#############
# CHANGELOG #
#############

# - BIG NEWS: Implement Flash update, both to the SRAM and/or the Flash memory
# - Cleared TMP directory on the Pico Flash at startup (lines 1582-1586)
# - Option for sorting DIR
# - Added logging function to 'activity.log' w/4 levels: INFO, WARNING, ERROR and CRITICAL. Notice CRITIAL not always means error,
#   but something that needs to be logged in any case
# - LOAD routine now validates block type, to avoid error on LOAD "" CODE for a BASIC pgm for instance
# - Implemented append newly SAVEd file to currently mounted TAP
# - Fixed small errors on mounting file and tap_idx references. Now mounting an already mounted file (remounting?)
#   behaves correctly, i.e. goes to the first block of the TAP
# - New, proper MOUNT_FILE() routine
# - LOAD now caches all files on internal Flash, and streams each byte (David's optimization)
# - Fixed LOADing non-existent filename from .TAP
# - Fixed special characters and trailing spaces in filename SAVE
# - New SAVE cmds: "tpi:blkrcv" [CODE n,m], "tpi:getlog" [CODE n, 0], "tpi:gethelp", "tpi:getinfo", "tpi:verbose", "tpi:append"
# - Incorrect commands now show description of error (if verbose=enabled)
# - Incorporated some try..except blocks in troublesome, failing parts
# - Two consecutives LOAD "" with no file mounted is now properly handled
# - TAP loop around now works 
# - Nonexistent/nonworking SD Card is now reported on the log and the TS-Pico is halted
# - Small cleanup here and there 

# TO DO:
#=======
# - Debug LPRINT, LLIST, etc
# - Add command to erase LOG file
# - LOAD and SAVE config.ini
# - GUI
# - Primary support for TZX, SNA and Z80 files
# - Test NMI routine to SAVE snapshots
# - Test "RST 8"-like ROM replacement with TS 2068 and/or Spectrum ROMs
#   for adding new, different OS versions that would also take advantage
#   of the TS-Pico hardware.
# - Add descriptive of each slot in the Flash in config.ini
# - "Golden commands" for Assembler
# - Dedicated SPI for the SD Card
# - Test special "update" firmware


import utime
import _thread
import time
import gc
import os
import json

from rp2 import StateMachine, asm_pio, PIO
from machine import Pin, freq, SPI

from TS.sdcard import *

from tspico_io import sel_bank, set_ctrl, set_dck, TS_IO, LOAD_TS, LOAD_ZX, LOAD_ZX_C, SAVE_TS, SAVE_ZX


#####################
# SERVICE FUNCTIONS #
#####################


class PICO_STATUS():                                                            # Class for the object that holds TS-Pico's current status
    
    def __init__(self, init_values):                                            # init_values is a dictionary read at startup; read below
                                                                                # The variables that define current status of the TS-Pico are:
        err_msg = "d"                                                                                
        err_st = 10
        
        self.append = False                                                     # whether or not append new SAVEd file to currently mounted TAP file
        self.bank_sm = 0                                                        # initial value for the BANK StateMachine
        self.cur_path = "/sd/TAP"                                               # string holding the current path
        self.f_name = []                                                        # string of current filename
        self.offset = 0                                                         # integer pointer to current position on a large TAP file
        self.offset_tbl = []                                                    # table of offsets for each segment in a .TAP file
        self.tap_idx = 0                                                        # pointer to position of next block to be LOADed in the mounted TAP 
        self.totlen = 0                                                         # integer holding total length in bytes, of a large TAP file
        self.zx48 = False                                                       # boolean for ZX Spectrum compatibility mode
        
        try:                                                                    # try to retrieve configuration values from init_values passed on startup

            self.DCK_SLOT = init_values["DCK_SLOT"]                             # What slot of Flash or SRAM contains the startup DCK image (0-15). default = 0 (Spectrum cartridge)
            self.ROM_SLOT = init_values["ROM_SLOT"]                             # What slot of Flash or SRAM contains the startup ROM image (0-15). default = 1 (TS-Pico ROM)
            self.ROM_SM = init_values["ROM_SM"]                                 # Bit pattern for Flash/SRAM activation during DCK/ROM access. Default = 0x0A, or 1010 meaning both assigned to Flash
            self.LOG_LEVEL = init_values["LOG_LEVEL"]                           # Log level: 0 info, 1 warning, 2 errors, 3 critical. Default = 1 
            self.VERBOSE = init_values["VERBOSE"]                               # Verbosity of status messages. Default = False, no verbosity. 

        except:                                                                 # if fail, assume hard-wired values
            
            self.DCK_SLOT = 0
            self.ROM_SLOT = 1
            self.ROM_SM = 10
            self.LOG_LEVEL = 2
            self.VERBOSE = False
            
            err_msg = "ERROR: Failed to load configuration values; using default hard-wired values"
            err_st = 2
            
        self.bank_sm = (self.DCK_SLOT * 16) + self.ROM_SLOT                    # bit pattern to store slot of DCK/ROM. 4 bits each. Default 0001 0000
    

def ACTIVATE_MQ():                                                                                # Re-enable TX/RX SM, after a SDCard access

    global MQ

    MQ = StateMachine(0, TS_IO, freq=15_000_000, out_base=Pin(2, Pin.OUT),
                      in_base=Pin(2, Pin.IN), jmp_pin=Pin(11),
                      sideset_base=Pin(12, Pin.OUT))
    
    MQ.active(1)
    
    return 
    

def ACTIVATE_SD():                                                                              # Enable SD-Card access SM, after TX/RX operation
    
    U3_CS       = Pin(28, Pin.OUT, Pin.PULL_UP)
    D0          = Pin(2,  Pin.IN)
    D1          = Pin(3,  Pin.IN)
    D2          = Pin(4,  Pin.IN)

    try:
        spi = SPI(0, sck=D0, mosi=D1, miso=D2)
        sd = SDCard(spi, U3_CS)
        os.mount(sd, "/sd")

    except:
        LOG("ERROR: Mounting SD Card failed in ACTIVATE_SD!", 2)
        SAVE_LOG()
        spi = -99
        
        while True:
            BLINK_ERROR()
        
    return spi


def BLINK_ERROR():                                                             # An onboard LED-blinking routine. This for an error condition. Interval is fixed

    global led
    
    led.value(1)

    for i in range(10):
        utime.sleep(.1)
        led.toggle()
    
    led.value(0)
        
    return


def BLINK_LED(pause):                                                           # Another routine that ...well...blinks the onboard LED!
                                                                                # Used by the COPY_FILE routine
    global dead
    global busy
    global led
    
    busy = True
    
    utime.sleep(.2)
    
    while not dead:
        led.value(1)
        utime.sleep(pause)                                                      # 'pause' controls interval
        led.value(0)
        utime.sleep(pause)
        
    led.value(0)
    busy = False
    
    return    


def CHK_STATUS(secs):                                                                                 # Watchdog that executes on the second thread, 
                                                                                                      # and kills the IO routine if needed.
    global MQ                                                                                                      
                                                                                                      
    global kill
    global dead
    global busy
    
    global led
    
    kill = False
    busy = True
    
    LOG("INFO: Starting watchdog...", 0)
    secs = secs * 1_000_000
    
    t_init = time.ticks_us()
    while (time.ticks_us() - t_init) < secs:
        if dead:
            break
    if not dead:
        LOG("ERROR: Abnormal termination. Clearing TX/RX FIFO....", 2)
        while not dead:
            MQ.exec("pull (noblock)")
            MQ.exec("mov (osr, null)")
            MQ.exec("mov (isr, null)")
            MQ.exec("push (noblock)")
            kill = True
             
        while MQ.rx_fifo() != 0:
            MQ.get()
        while MQ.tx_fifo() != 0:
            MQ.exec("pull (noblock)")
            MQ.exec("set (osr, null)")
        MQ.active(0)
        
        LOG("INFO: TX/RX FIFO successfully cleared. Operation finished", 0)
        
        BLINK_ERROR()
        
        MQ.active(1)
        
        LOG("INFO: Ending watchdog. Operation ended normally", 0)
        
    kill = False
    busy = False
    
    return


def COPY_FILE(src_file, dst_file):                                                          # Copy the large .TAP file to Pico's internal flash
                                                                                             # best compatibility and performance
    global dead
    global busy
    global led
    
    dead = False
    
    buf = bytearray(512)
    bytes_rd = 0
    
    _thread.start_new_thread(BLINK_LED, (0.1, ))                                          

    with open(src_file, 'rb') as file_in:
        with open(dst_file, 'wb') as file_out:
            
            bytes_rd = file_in.readinto(buf)
            
            while bytes_rd  > 0:
                file_out.write(buf[:bytes_rd])
                bytes_rd = file_in.readinto(buf)
                            
    led.value(0)
    dead = True
    
    del buf                                                                             # OPTIMIZATION - CHECK!       
    gc.collect()
    
    while busy:
        pass
    
    return


def DCK_IMAGE():                                                                              # Generates a full 64Kb image from a .DCK file
                                                                                              # This will be used by the Flash write pgm
    global TSP

    header = bytearray(9)
    chunk_len = 8192
    empty = bytearray(chunk_len)
    cur_chunk = bytearray(chunk_len)
    
    LOG("INFO: Start processing DCK file", 0)
    
    try:
        os.remove("/TMP/temp.bin")
    except:
        pass

    f_in = open(TSP.f_name, "rb")
    f_out = open("/TMP/temp.bin", "wb")

    f_in.readinto(header)

    if header[0] != 0x00:
        LOG("CRITICAL ERROR! Not a DOCK image; aborting...", 3)
        
        f_in.close()
        f_out.close()
        
        return

    LOG("INFO: DCK header:" + str(header), 0)

    for el in range(1, 9):
        if header[el] == 0x02:
            f_in.readinto(cur_chunk)
            f_out.write(cur_chunk)
        elif header[el] ==0x00:
            f_out.write(empty)
        else:
            LOG("CRITICAL ERROR! Not a DOCK image; aborting...", 3)
            return

    LOG("INFO: Image of DCK file generated succesfully", 0)
    
    f_in.close()
    f_out.close()
    
    return


def DIR_FILES():                                                                             # Get all files and directories from current path
    
    global files
    global lista
    
    files = []
    lista = ""
    header = ""
    
    dirinfo = []
    tap_blk = []
    tap_hdr = []
    num_dirs = 0
    num_files = 0
    
    ext = ['TAP', 'TZX', 'DCK', 'ROM', 'BIN']                                                 # extensions to be included 
    starts = ['.']                                                                            # first characters of files to be excluded
    
    ordered = True                                                                            # In the future, this could be controlled by an option
    
    try:
        os.remove("dirinfo.tap")
    except:
        pass
    
    if ordered:
        listing = sorted(os.ilistdir(), key=lambda fname: fname[0].lower())
    else:
        listing = [item for item in os.ilistdir()]
    
    sd_block = os.statvfs("")[0]
    sd_tot = os.statvfs("")[2]
    sd_free = os.statvfs("")[3]
    
    sd_free = (sd_free * sd_block) / 1_073_741_824
    sd_tot = (sd_tot *sd_block) / 1_073_741_824
    
    sd_stat = "SD: " + '%02.4f' % (sd_tot ) + "GB; free: " + '%02.4f' % (sd_free) + "GB"
    sd_stat = "%-32s" % (sd_stat)

    for dirs in listing:
        if dirs[1] == 16384:
            nom = dirs[0][:20]
            new_item = ("%-32s" %  nom )
            dirinfo.append(new_item)
            lista += "%-22s" % ("<" + nom + ">") + "%10s" % "0 b"
            
    num_dirs = len(dirinfo)
    
    i = 0
    
    for archs in listing:
        if archs[1] == 32768:
            if (archs[0][-3:].upper() not in ext) or (archs[0][0] in starts):
                continue
            
            nom = "%03d" % i
            nom = nom + ' ' + "%-18s" % archs[0]
            nom = nom[:22]
            size = int(archs[3])
            if size >= 1024:
                size = size / 1024
                size_txt = "%.2f" % (size) + " Kb"
            else:
                size_txt = str(size) + " b"
            lista += nom + "%10s" % (size_txt)
            new_item = (nom + "%10s" % (size_txt))
#             new_item = new_item[4:]
            dirinfo.append(new_item)
            files.append(archs[0])
            
            i += 1
            
    header = "Path:" + public_path()
    header = header[:32]
    header = "%-32s" % (header)
    header += sd_stat 
    header += "%-22s" % "File Name" + "%-10s" % "    Size"  
    header += "--------------------------------"
    
    if not lista:
        lista = "%-32s" % ("Directory is empty")
    lista = header + lista

    num_files = len(dirinfo) - num_dirs
    
    new_item = "%-32s" % (num_dirs)
    dirinfo.insert(0, new_item)
    
    new_item = "%-32s" % (num_files)
    dirinfo.insert(1, new_item)
    
    tap_blk = (NEW_TAPBLK(dirinfo, 32))
    long = len(tap_blk) - 4                                        # this is the pure data blk size stored in header; it's the block minus the first 4 bytes
    fname = "dirinfo"
    tap_hdr = NEW_HDR(2, fname, long)                             # generate header for each block, with parameters
    
    with open("dirinfo.tap", "wb") as f_out:
        f_out.write(tap_hdr)                                          # now write the header
        f_out.write(tap_blk)                                           # and then the block

    return 


def LOG(msg, level):                                                                    # Adds a timestamped new entry to log_entries
    
    global log_entries
    global TSP
    
    if TSP.LOG_LEVEL:                                                                    # TSP is not initialized at startup, so this check is required
        if level < TSP.LOG_LEVEL:
            return
    
    log_entries += "[" + str(time.ticks_us()) + "] "                                    # on Pico W, timestamp can be replaced by local time provided by ntp
    log_entries += msg + "\n"
    
    return


def MOUNT_FILE():                                                                            # Mount file from a LOAD "tpi:..." command 
                                                                                             # and performs actions according to file type
    global TSP
    global led

    led.value(1)
    
    img = []
    
    TSP.offset = 0
    TSP.tap_idx = 0
    TSP.offset_tbl = []
    
    TSP.append = False

    try:
        os.remove("/TMP/temp.tap")
        os.remove("/TMP/temp.bin")
    except:
        pass
    
    msg = "INFO: File " + TSP.f_name + " mounted correctly"
    err_level = 0
    
    ACTIVATE_SD()
    
    TSP.totlen = os.stat(TSP.f_name)[6]
    
    if TSP.f_name[-4:].upper() in [".BIN", ".DCK", ".ROM"]:
        
        COPY_FILE(TSP.f_name, "/TMP/temp.bin")
        
        if TSP.f_name[-4:].upper() == ".DCK":
        
            DCK_IMAGE()
            COPY_FILE("/TS/dckupdate.tap", "/TMP/temp.tap")              # Special 'seudo' TAP that contains Flash/SRAM DCK update program
    
        else:
            
            len_hi = int(TSP.totlen / 256)
            len_lo = TSP.totlen - (len_hi * 256)

            with open("/TS/romupdate.tap", "rb") as f_in:                 # Same for updating ROM images. We open the seudo TAP, as we need to update it
                buf = bytearray(f_in.read())
            
            buf[2504] = len_lo                                           # We update the TAP file ML routine, with the length of the block
            buf[2505] = len_hi                                           # to be written to the Flash/SRAM

            buf[2704] = len_lo                                           # Same to the second part of the ML routine (Update LOWER block)
            buf[2705] = len_hi
            
            with open("/TMP/temp.tap", "wb") as f_out:                            # And we update the seudo TAP
                f_out.write(buf)
        
    elif TSP.f_name[-4:].upper() == ".TAP":
        
        COPY_FILE(TSP.f_name, "/TMP/temp.tap")
        OFF_TABLE()
            
    else:
        msg = "ERROR!: Wrong filename while mounting: " + TSP.f_name
        err_level = 2
        
    LOG(msg, err_level)
    led.value(0)
    
    try:
        TSP.totlen = os.stat("/TMP/temp.tap")[6]                                       # We mount this file as a regular TAP to perform Flash write
    except:
        pass
    
    try:
        os.umount("/sd")
    except:
        pass
    
    return
        

def NEW_HDR(type_hdr: int, fname, long: int):                      # This routine returns a new TAP header with the required parameters: header type, file name, and length of data block
    
    if (long < 0 or long > 65535):                                 # Validate data block length
        LOG("ERROR!!! Wrong block length in NEW_HDR", 2)
        return
    
    if (type_hdr > 3) or (type_hdr < 0):
        LOG("ERROR!!! Wrong header type in NEW_HDR", 2)                  # Also validate header type 
        return
    
    hdr = bytearray.fromhex('00')                                  # We start building the bytearray that will form the header: start with 0x00, a type header (FF=data)
    hdr += type_hdr.to_bytes(1, 'little')                          # Next, the filename passed as parameter
    hdr += f"{fname:<10}"[:10]                                     # ...trimmed to 10 bytes and left-justified with blanks
    
    long_b = int(long/256)                                         # Now we calculate LSB and MSB of block length
    long_a = int(((long/256) - long_b) * 256)
    
    hdr += long_a.to_bytes(1, 'little') + long_b.to_bytes(1, 'little')   #... and add it to the header
    hdr += bytearray.fromhex('69c18080')                           # Next, four bytes of which the second indicates array letter; the rest are ignored    
                                                                   # As we always use the same variable name ('a'), this pattern never changes
    crc = 0                                                        # Now we calculate the CRC for the entire block
    for el in hdr:
        crc = crc ^ el
        
    hdr += crc.to_bytes(1, 'little')                               #... and append it to the end of the block
    
    hdr = bytearray.fromhex('1300') + hdr                          # Now we add the (fixed) length for the header
    
    return(hdr)                                                    # and return the header
    

def NEW_TAPBLK(items, maxsize: int):                               # This routine generates a data block for storing an array, with the parameters: array items, and max size of single item
    
    num_items = len(items)

    dims = [0] * 4                                                 # This will hold LSB and MSB for both dimension of the array

    dims[1] = int((num_items)/256)  
    dims[0] = int(((num_items/256) - dims[1]) * 256)

    dims[3] = int((maxsize)/256)
    dims[2] = int(((maxsize/256) - dims[3]) * 256)

    blk = bytearray.fromhex("FF02")                                # We start a new data block: FF for data, 02 for String array type

    for el in dims:
        blk += el.to_bytes(1, 'little')                            # Now, store each LSB/MSB in blk
        
    for el in items:                                               # Now onto the items themselves 
        blk += el
    
    crc = 0
    for el in blk:
        crc = crc ^ el                                             # calculate CRC
    
    blk += crc.to_bytes(1, 'little')                               # and store it at the end of the blk
    
    len_blk = len(blk)
    len2 = int((len_blk)/256)                                      # Now calculate blk length's LSB/MSB 
    len1 = int(((len_blk/256) - len2) * 256)
    
    blk = len2.to_bytes(1, 'little') + blk                         #...and store it on the blk's first two positions
    blk = len1.to_bytes(1, 'little') + blk

    return(blk)                                                    # and return the blk


def OFF_TABLE():                                                             # Builds an offset table of segments, from the current .TAP file
    
    global TSP
    
    arch = open("/TMP/temp.tap", "rb")
    offset_tbl = []
    
    blks = ['Program', 'Number arr.', 'Char arr.', 'Code blk']
    
    while TSP.offset < TSP.totlen:
        rd_bytes = bytearray(30)    
        arch.seek(TSP.offset)
        arch.readinto(rd_bytes)
        long = rd_bytes[0] + (256*rd_bytes[1])
        
        code_blk = rd_bytes[2]

        if (code_blk == 0):
            hdr = " Y"
            try:
                name = rd_bytes[4:14].decode()
                blk_type = blks[rd_bytes[3]]
            except:
                name = "??????????"
                blk_type = "undefined"
        else:
            hdr = " N"
            name = blk_type
            
        values = [TSP.offset, long, hdr, name]
        TSP.offset_tbl.append(values)
            
        long += 2
        TSP.offset += long
        
    TSP.offset = 0
    del rd_bytes
    
    arch.close()
    gc.collect()
    
    return


def PERFORM_UPDATE():
    
    global led
    
    try:
        os.chdir("/sd/UPD")
        update = True
        
    except:
        update = False
        
    if update:
        
        success = True
        
        led.value(1)
        
        LOG("CRITICAL: UPD found, starting update process.", 3)
        SAVE_LOG()
        
        with open ("update.json", "r") as upd_file:
            upd_init = json.load(upd_file)
        
        for el in upd_init["dirs"]:
            
            if not success:
                break
            
            try:
                REMOVE_DIR(el)
            except:
                pass
            
            try:
                os.mkdir(el)
                
            except:                
                LOG("CRITICAL: Unable to create folder " + el + " during Update. Deleting /sd/UPD and aborting.", 3)
                SAVE_LOG()
                
                success = False
                
        for el in upd_init:
            
            if not success:
                break
        
            if el == "dirs":
                continue
            
            try:
                COPY_FILE(el, upd_init[el]+el)
            except:
                LOG("CRITICAL: Unable to copy file " + el + " during Update. Deleting /sd/UPD and aborting.", 3)
                SAVE_LOG()
                
                success = False

        if success:
                
            LOG("CRITICAL: UPDATE finished successfully. Cleaning up update files.", 3)
            
            os.chdir("/sd")
            REMOVE_DIR('/sd/UPD')
            
            LOG("CRITICAL: All update files cleaned up. Waiting for shutdown.", 3)
            SAVE_LOG()
            
            os.umount("/sd")
            
            while True:
                led.toggle()
                utime.sleep(1)
        else:        
            
            os.chdir("/")
            REMOVE_DIR("/sd/UPD")
            os.umount("/sd")
            
            while True:
                BLINK_ERROR()
            
    return


def SAVE_LOG():                                                                         # Saves log_entries to the 'activity.log' file in flash
    
    global busy
    global log_entries
    
    busy = True
    
    with open("/activity.log", "a") as logfile:
        logfile.write(log_entries)
        
    log_entries = ""
    
    busy = False

    return


def SEND_MSG(msg, msg1, st: bytes):                                                             # Sends one-line status message(s) 
                                                                                                # back to the TS, once a command is finished
    global MQ
    global TSP
    
    wrt = MQ.put
    
    if TSP.VERBOSE:
    
        wrt(0x40)
        wrt(0x81)
        wrt(st)
        wrt(0x0D)
        for m in msg:
            wrt(m)
        if msg1:
            wrt(0x0D)
            for m in msg1:
                wrt(m)
        wrt(0x00)
        
    else:
        
        wrt(0x40)
        wrt(st)
        
    while(MQ.tx_fifo() !=0):
        pass
    
    return


def SEND_MSG2(msg, st: bytes):                                              # Sends a SCROLLING status message back to the TS,
                                                                                              # once a command is finished
    global MQ                                                                                          
                                                                                                  
    global kill
    global dead
        
    wrt = MQ.put
    r = range(640)
    
    scroll = "press N to stop: "
    
    wrt(0x40)
    wrt(0x86)
    wrt(st)
    wrt(0x0D)
    
    fff = MQ.get()
    
    while True:
        
        dead = False

#         while busy:
#             pass
#         _thread.start_new_thread(CHK_STATUS, (MQ, 5))

        wrt(0x0D)
        for i in r:
            wrt(msg[i])
        wrt(0x0D)        
        for m in scroll:
            wrt(m)
            
        dead = True
        
        if kill:
            LOG("ERROR: SEND_MSG2 failed! " + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 2)
            return
            
        wrt(0x00)
        wrt(0x64)
        
        if (MQ.get() == 78):
            wrt(0x00)
            return
        
        msg = msg[640:]
        
        if not msg:
            wrt(0x00)
            break
        
        if (len(msg) <= 672):
            r = range(len(msg))
            scroll = "--- End of list (N to exit) ---"
            
        else:
            r = range(672)
        
        LOG("INFO: SEND_MSG2 finished. " + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 0)
    
    return


##########################
# LOAD COMMAND FUNCTIONS #
##########################


def LD_NOT_IMP():                                                                       # Output for not implemented LOAD Command 
    
    SEND_MSG("CMD OK but not yet implemented", "", 4)
    
    return


def DIR():                                                                              # Directory listing

    global TSP
    global lista
    global led

    led.value(1)
    
    if len(lista) <= 672:                                                                # if single screen call message routine with no scroll
        prev_VERBOSE = TSP.VERBOSE
        TSP.VERBOSE = True
        SEND_MSG(lista, "", 1)
        TSP.VERBOSE = prev_VERBOSE
    else:
        SEND_MSG2(lista, 1)                                                                    # if not, call scrolling message routine
        
    led.value(1)
    utime.sleep(2)
    led.value(0)
   
   
def PATH():                                                                             # Show current directory
    
    global TSP
    
    prev_VERBOSE = TSP.VERBOSE
    TSP.VERBOSE = True
    SEND_MSG("Current working dir is: ", public_path(), 1)
    TSP.VERBOSE = prev_VERBOSE
    
    return
    

def TAPDIR():                                                        # Display contents of currently mounted TAP file
    
    global TSP
    
    if TSP.offset_tbl:
        nom = "File :" + TSP.f_name
        
        if len(nom) > 32:
            nom = nom[:15] + ".." + nom[-15:]
        else:
            nom = "%-32s" % (nom)
        nom += "Pointer now on block: %02d        " % TSP.tap_idx
        nom += " #  Offset   Len  Hdr?   Desc.  "
        nom += "--------------------------------"
        
        idx = 0

        for el in TSP.offset_tbl:
            if idx == TSP.tap_idx:
                nom += ">%02d " % idx
            else:            
                nom += " %02d " % idx
                
            nom += "%6s  " % el[0]
            nom += "%5s " % el[1]
            nom += el[2] + "  "
            nom += "%-10s" % el[3]
            
            idx += 1
            
    else:
        nom = " --  No .TAP file mounted!  --  "
        LOG("WARNING: no file mounted in TAPDIR", 1)
        
    if len(nom) <= 672:                                                             # if single screen call message routine with no scroll
        prev_VERBOSE = TSP.VERBOSE
        TSP.VERBOSE = True
        SEND_MSG(nom, "", 1)
        TSP.VERBOSE = prev_VERBOSE
    else:
        SEND_MSG2(nom, 1)                                                               # if not, call scrolling message routine

    return


##########################
# SAVE COMMAND FUNCTIONS #
##########################


def SA_NOT_IMP(pre, cmd):                                                      # Output for not implemented SAVE Command 
    
    SEND_MSG("CMD OK, but not yet implemented", "", 4)

    return


def dir_exists(filename):                                                                              # Checks whether filename's directory exists or not
    try:
        return (os.stat(filename)[0] & 0x4000) != 0
    except OSError:
        return False
        
        
def file_exists(filename):                                                                             # Checks whether filename exists or not
    try:
        return (os.stat(filename)[0] & 0x4000) == 0
    except OSError:
        return False
    
    
def public_path():                                                                                     # Returns the public version of the path
    
    global TSP
    
    try:
        #cur_path = os.getcwd()
        return ("/" + TSP.cur_path[8:])
    
    except OSError:
        return "OS Error"
    

def APPEND(pre, cmd):                                                                                  # Start appending each newly SAVEd file to currently mounted TAP

    global TSP
    
    if TSP.f_name:
        TSP.append = True
        SEND_MSG("Append new file to: ", TSP.f_name, 1)
    else:
        SEND_MSG("No file mounted. Append failed", "", 4)

    return 


def BLKRCV(pre, cmd):                                                                                  # 'Internal' command to send block to be written to Flash
    
    global MQ
    global TSP
    global led
    
    wrt = MQ.put
    
    status = 1
    buf = []
    
    led.value(1)
    
    if TSP.f_name[-4:].upper() == ".DCK":
        
        wrt(0x40)
        wrt(status)
        
        buf = bytearray(32768)
        
        with open("/TMP/temp.bin", "rb") as file:
            
            for i in range(2):
                file.readinto(buf)
                for el in buf:
                        wrt(el)
                        
        del buf
        gc.collect()
        
        LOG("INFO: DCK image write successfully completed", 0)
        
    elif TSP.f_name[-4:].upper() in [".BIN", ".ROM"]:
        
        file_len = os.stat("/TMP/temp.bin")[6]
        send_len = file_len
        
        par1 = (pre[4] * 256) + pre[3]
        par2 = (pre[6] * 256) + pre[5]
        
        if ((par1 + par2) > file_len):
            status = 3
            BLINK_ERROR()
        
        wrt(0x40)
        wrt(status)
        
        if (status == 1):
            
            rd_offset = par2
            
            if (par1 != 0):
                send_len = par1
            else:            
                send_len = file_len - rd_offset
            
            buf = bytearray(send_len)
            
            with open("/TMP/temp.bin", "rb") as file:
                file.seek(rd_offset)
                file.readinto(buf)
                
            for el in buf:
                    wrt(el)
                    
            del buf            
            gc.collect()
            
        led.value(0)
        
        LOG("INFO: ROM image write successfully completed", 0)
    
    return


def CDIR(pre, cmd):                                                                                            # Changes path to specified DIRectory
    
    global TSP
    
    global files
    global lista
    
    status = 1
    
    ACTIVATE_SD()
    
    potential_new_path = cmd[10:]
    if potential_new_path == ".." and TSP.cur_path.count("/") > 2:
        # remove the last element from the current path
        # unless the last element is TAP
        #print("attempt to move up one directory")
        path_list = list(TSP.cur_path.split("/"))       # convert current path to a list
        path_list.pop(0)  # remove the first element, which is blank
        path_list.pop()   # remove the last element
        new_path = "/".join(path_list)
        
    elif potential_new_path == "/":
        # move to the top
        new_path = "/sd/TAP"
          
    elif dir_exists(TSP.cur_path + "/" + potential_new_path):
        # it's a valid path
        new_path = TSP.cur_path + "/" + potential_new_path
    else:
        # no changes bc it doesn't meet any of the tests above
        new_path = TSP.cur_path
        status = 3
    
    #new_path = cur_path + "/" + cmd[10:]
    #print (cur_path,new_path)
    #os.chdir(cur_path)

    #message = "Changed dir to: "  + cmd[10:]
    #status = 1
    
    os.chdir(new_path)
    TSP.cur_path = os.getcwd()
    
    if status == 1:
        message = "Changed dir to: "  + cmd[10:]
    else:
        message = "OS error changing to: "  + cmd[10:]
        LOG("ERROR: " + message, 2)
        
    gc.collect()
    DIR_FILES()
    os.umount("/sd")
    
    ACTIVATE_MQ()
    
    SEND_MSG(message, "Current: " + public_path(), status)
    
    return


def FWD(pre, cmd):                                                                                     # Moves pointer to next block in TAP file; also 
                                                                                                       # can skip 'CODE n' # of blocks forward
    global TSP
    
    num_blks = len(TSP.offset_tbl) - 1
    
    if pre[3] != 0:
        forth = pre[3]
    else:
        forth = 1
    
    if TSP.tap_idx >= num_blks:
        
        msg = "Can't FWD. Already on last block"
        st = 4
        
    else:
        TSP.tap_idx += forth
        if TSP.tap_idx >= num_blks:
            TSP.tap_idx = num_blks
            
        TSP.offset = TSP.offset_tbl[TSP.tap_idx][0]
        gc.collect()

        msg = "Moved ahed to block # " + str(TSP.tap_idx)
        st = 1

    SEND_MSG(msg, "", st)
    
    return 


def GETHELP(pre, cmd):                                                 # Shows TS-Pico internal status

    global TSP
    
    prev_VERBOSE = TSP.VERBOSE
    
    nl = chr(13)
    
    msg = "%-32s" % ('LOAD cmds')
    msg += "%-32s" % ('========')
    msg += "%-32s" % ('"tpi:dir"  ')
    msg += "%-32s" % ('"tpi:path" ')
    msg += "%-32s" % ('"tpi:tapdir" ')
    msg += "%-32s" % (' ')
    msg += "%-32s" % ('SAVE cmds: []-> optional')
    msg += "%-32s" % ('=========================')
    msg += "%-32s" % ('"tpi:blkrcv" [CODE n,m]')
    msg += "%-32s" % ('"tpi:blksnd" [CODE n,0]')
    msg += "%-32s" % ('"tpi:cd <name>"')
    msg += "%-32s" % ('"tpi:close" ')
    msg += "%-32s" % ('"tpi:ffw" [CODE n,0]')
    msg += "%-32s" % ('"tpi:gethelp"')
    msg += "%-32s" % ('"tpi:getinfo"')
    msg += "%-32s" % ('"tpi:getlog" [CODE n,0]')
    msg += "%-32s" % ('"tpi:md <folder>"')
    msg += "%-32s" % ('"tpi:memboot" CODE n,m')
    msg += "%-32s" % ('"tpi:memdock" CODE n,m')
    msg += "%-32s" % ('"tpi:rm <folder>"')
    msg += "%-32s" % ('"tpi:rew" [CODE n,0]')
    msg += "%-32s" % ('"tpi:sdcard"')
    msg += "%-32s" % ('"tpi:tape"')
    msg += "%-32s" % ('"tpi:verbose"')
    msg += "%-32s" % ('"tpi:zx48"')
    
    TSP.VERBOSE = True
    
    SEND_MSG2(msg, 1)

    TSP.VERBOSE = prev_VERBOSE 

    return


def GETINFO(pre, cmd):                                                 # Shows TS-Pico internal status

    global TSP
    global files
    global lista
    
    prev_VERBOSE = TSP.VERBOSE
    TSP.VERBOSE = True
    
    cop = chr(127)
    nl = chr(13)
    sd_stat = lista[32:63]
    
    fl_block = os.statvfs("")[0]
    fl_tot = os.statvfs("")[2]
    fl_free = os.statvfs("")[3]

    fl_free = (fl_free * fl_block) / 1_048_576
    fl_tot = (fl_tot * fl_block) / 1_048_576
    
    fl_stat = ">Flash: " + '%02.2f' % (fl_tot ) + "MB; free " + '%02.2f' % (fl_free) + "MB"
    fl_stat = "%-32s" % (fl_stat)

    memfree = '%06.2f' % (gc.mem_free() / 1024)
    
    msg = " * TS-Pico interface status *" + nl
    msg += cop + " 2023, 2024 TS Pico Dev Team" + nl
    msg += "--------------------------------"
    msg += ">FW Rev.: 1.1; uPython: 1.22.0" + nl
    msg += ">Board Rev.: V2.2" + nl
    msg += ">Pico Free RAM: " + memfree + " Kb." + nl
    msg += fl_stat
    
    msg += ">Append: " + str(TSP.append)
    msg += "; Verbose: " + str(prev_VERBOSE) + nl
    msg += ">Mounted file: " 
        
    if TSP.f_name:
        msg += "/" + TSP.f_name[8:] + nl
    else:
        msg += "none" + nl
    
    msg += ">" + sd_stat
    msg += ">Current path: " + public_path() + nl
    msg += ">Files in dir: " + str(len(files)) + nl
    
    SEND_MSG(msg, "", 1)

    TSP.VERBOSE = prev_VERBOSE

    return


def GETLOG(pre, cmd):                                                 # Shows the last nn bytes of the events log file 

    global TSP
    global led
    
    led.value(1)
    
    log_fname = "/activity.log"
    
    file_seek = 0
    log_content = ''
    
    len_cmd = (pre[4] * 256) + pre[3]
    len_file = os.stat(log_fname)[6]
    
    if len_cmd != 0 and (len_cmd <= len_file):
        len_read = len_cmd
        file_seek = len_file - len_cmd
    else:    
        len_read = len_file

    msg = bytearray(len_read)

    with open(log_fname, "r") as logfile:
        
        if file_seek:
            logfile.seek(file_seek)
            
        logfile.readinto(msg)
            
    for i in range(len(msg)):
        if msg[i] == 0x0A:
            msg[i] = 0x0D
    
    if len(msg) <= 672:                                                                # if single screen call message routine with no scroll
        prev_VERBOSE = TSP.VERBOSE
        TSP.VERBOSE = True
        SEND_MSG(msg, "", 1)
        TSP.VERBOSE = prev_VERBOSE
    else:
        SEND_MSG2(msg, 1)                                                                    # if not, call scrolling message routine
        
    led.value(0)
    
    return


def LOAD_CONFIG():
        
    init_values = []
    return_values = []
    
    try:
        with open("config.ini", "r") as f:                      # We first try to load config values from config.ini file
            init_values = json.load(f)
            
        if (init_values["ROM_SM"] <= 4) or (init_values["ROM_SM"] in [8, 12]):
            LOG("ERROR: Incorrect initial ROM_SM value. Using default values instead", 2)
            init_values["ROM_SM"] = 10
                
        if init_values["ROM_SLOT"] != 1:                                   # If we started with a non-default ROM slot, we use it on this run,
                                                                           # but reverse back to default hard-wired 1 for next boot (after power-cycle the Pico)
            return_values = init_values                                                                       
            init_values["ROM_SLOT"] = 1
            
            try:
                with open("config.ini", "w") as f:
                    json.dump(init_values, f)
            except:
                LOG("ERROR: while updating config.ini!", 2)
                SAVE_LOG()
            
            init_values = return_values
            
    except:                                                     # If fails, we load default hard-wired values
        
        LOG("WARNING: Failed to load initial values from config.ini. Using default values instead", 1)
        init_values["DCK_SLOT"] = 1                             # Slot in Flash for DCK image at startup
        init_values["ROM_SLOT"] = 0                             # Slot in Flash for ROM image at startup
        init_values["ROM_SM"] = 10                              # Flash/SRAM activation pattern bitmap for DCK access (MSB=10) and ROM access (LSB=10)
        init_values["LOG_LEVEL"] = 2                            # Only log errors and up
        init_values["VERBOSE"] = False                          # Disable verbosity on commands
            
    SAVE_LOG()
    
    return init_values            


def MDIR(pre, cmd):                                                                                         # MAKE DIRectory in the current path                         
    
    global TSP
    
    ACTIVATE_SD()
    os.chdir(TSP.cur_path)
    
    message = "Created dir: "  + cmd[10:]
    status = 1
    
    try:
        os.mkdir(cmd[10:])
        DIR_FILES()
        
    except OSError:
        
        message = "OS error creating: "  + cmd[10:]
        LOG("ERROR: " + message, 2)
        status = 3
    
    os.umount("/sd")
    ACTIVATE_MQ()
    
    SEND_MSG(message, "", status)
    
    return 
                

def MEMBOOT(pre, cmd):                                           # Changes ROM slot to boot from; either SRAM or Flash
    
    global TSP
    
    global BANK
    global ROM
    
    par1 = (pre[4] * 256) + pre[3]
    par2 = (pre[6] * 256) + pre[5]
    
    if (par1 == 0 or par1 > 3 or par2 > 15):
        SEND_MSG('Wrong values, MEM=' + str(par1) + ', PAGE=' + str(par2), "OK values: MEM=1..3, PAGE=0..15", 4)
        LOG("WARNING: Wrong values in MEMBOOT, MEM=" + str(par1) + ", PAGE=" + str(par2) + ". Command ignored", 1) 
    else:            
        val1 = TSP.ROM_SM & 12
        TSP.ROM_SM = val1 + par1
        
        val1 = TSP.bank_sm & 240
        TSP.bank_sm = val1 + par2
        
        with open("config.ini", "r") as f:                                                    # As sometimes this change can hang the machine,
            init_values = json.load(f)                                                        # we modify the init values for next startup
                                                                                              # so changes will take effect next reboot
        init_values["ROM_SLOT"] = par2
        
        with open("config.ini", "w") as f:
            json.dump(init_values, f)
            
        SEND_MSG('Change ROM to MEM=' + str(par1) + ', PAGE=' + str(par2), "", 1)
        LOG("INFO: Change ROM to MEM=" + str(par1) + ", PAGE=" + str(par2) + " in MEMBOOT", 0)
        
        ROM.put(TSP.ROM_SM)
        BANK.put(TSP.bank_sm)
        
#         while(MQ.tx_fifo() != 0):
#             pass

    return 


def MEMDOCK(pre, cmd):                                                   # Changes DCK slot; either SRAM or Flash

    global TSP
    
    global BANK
    global ROM
    
    par1 = (pre[4] * 256) + pre[3]
    par2 = (pre[6] * 256) + pre[5]
    
    if (par1 == 0 or par1 > 3 or par2 > 15):
        SEND_MSG('Wrong values, MEM=' + str(par1) + ', PAGE=' + str(par2), "OK values: MEM=1..3, PAGE=0..15", 4)
        LOG("WARNING: Wrong values in MEMDOCK, MEM=" + str(par1) + ", PAGE=" + str(par2) + ". Command ignored", 1) 
    else:            
        val1 = TSP.ROM_SM & 3
        TSP.ROM_SM = val1 + (par1 * 4)
        val1 = TSP.bank_sm & 15
        TSP.bank_sm = val1 + (par2 * 16)
        
        SEND_MSG('Change DCK to MEM=' + str(par1) + ', PAGE=' + str(par2), "", 1)
        LOG("INFO: Change DCK to MEM=" + str(par1) + ", PAGE=" + str(par2) + " in MEMDOCK", 0)
        
        ROM.put(TSP.ROM_SM)
        BANK.put(TSP.bank_sm)
        
    return 


def REMOVE_DIR(d):                                                        # Recursively remove a directory and all its contents
    
    try:
        if os.stat(d)[0] & 0x4000:  # Dir
            for f in os.ilistdir(d):
                if f[0] not in ('.', '..'):
                    REMOVE_DIR("/".join((d, f[0])))  # File or Dir
            os.rmdir(d)
        else:  # File
            os.remove(d)
        
    except:
        LOG("WARNING: could not remove directory " + d, 1)
        
    return


def REW(pre, cmd):                                                                                           # Moves pointer to next block in TAP file; also 
                                                                                                             # can skip 'CODE n' # of blocks backwards
    global TSP
    
    if pre[3] != 0:
        back = pre[3]
    else:
        back = 1
    
    if TSP.tap_idx <= 0:
        msg = "Can't REW. Already on 1st block"
        st = 4
        
    else:
        TSP.tap_idx -= back
        if TSP.tap_idx <= 0:
            TSP.tap_idx = 0
            
        TSP.offset = TSP.offset_tbl[TSP.tap_idx][0]

        msg = "Moved back to block # " + str(TSP.tap_idx) 
        st = 1
        
    SEND_MSG(msg, "", st)

    return

    
def RMDIR(pre, cmd):                                                        # Output for not implemented SAVE Command 
    
    global TSP
    
    ACTIVATE_SD()
    os.chdir(TSP.cur_path)
    
    message = "Removed dir: "  + cmd[10:]
    status = 1
    
    try:
        os.rmdir(cmd[10:])
        DIR_FILES()
        
    except OSError:
        
        message = "OS error removing: "  + cmd[10:]
        LOG("ERROR: " + message, 2)
        status = 3
    
    os.umount("/sd")
    ACTIVATE_MQ()
    
    SEND_MSG(message, "", status)
    
    return 
                

def UNMOUNT(pre, cmd):                                                                                       # Unmount currently mounted file 
    
    global TSP
    
    SEND_MSG("Unmounting file. ", "", 1)
    
    TSP.f_name = []
    TSP.offset_tbl = []
    TSP.tap_idx = 0
    TSP.append = False
    
    try:
        os.remove("/TMP/temp.bin")    
        os.remove("/TMP/temp.tap")    
    except:
        pass
    
    return 


def VERB_TOGGLE(pre, cmd):                                                                               # Toggle commands verbosity ON/OFF 
    
    global TSP
    
    TSP.VERBOSE = not(TSP.VERBOSE)
    
    if TSP.VERBOSE:
        msg = "Verbose is now enabled"
    else:    
        msg = "Verbose is now disabled"
    
    SEND_MSG(msg, "", 1)

    return 


def ZX48(pre, cmd):                                                           # Changes to ZX Spectrum 48 compat mode 
    
    global TSP
    
    TSP.zx48 = True
    
    SEND_MSG('Changing to ZX48 mode. To returnto TS, type: SAVE "OUT 10, 100"', "", 1)
            
    return 


##################################
# PRE HEADER PROCESSING ROUTINES #
##################################


def PRINT_IO(pre):                                                                                                           # LPRINT and LLIST processing
    
    global MQ
    global TSP
    
    prn = bytearray(10000)
    end_msg = "File 0001.txt closed OK"
    r1 = range(10)
    wrt = MQ.put

    pos = 0
    while True:
        prn[pos] = pre[3]
        pos += 1
        
        wrt(0x40)
        wrt(0x01)
        
        pre = [0] * 10
        for i in r1:
            pre[i] = MQ.get()
        if pre[1] != 5:
            break
    
    wrt(0x40)
    wrt(0x01)
    
    SEND_MSG(end_msg, "", 1)
    
    while (MQ.tx_fifo() != 0):
        pass
  
    while (MQ.rx_fifo() != 0):
        fff = MQ.get()
        
    prn = prn[:pos]
    
    with open("/PRN/0001.txt", "w") as sal:                                           # PRINT output filename is fixed on this version; can be set up
            sal.write(prn)                                                            # in future version

    return


def PROCESS_ASM(pre):                                                                 # Processes AU (Assembler) commands sent by the TS
    
    global MQ
    
    cmd = pre[:5].decode()
    wrt = MQ.put
    
    wrt(0x40)
    
    print(pre)
    print(cmd)
    
    par3 = int(pre[8])
    par4 = int(pre[9])
    
    print(par3, par4)
    
    wrt(0x40)
    wrt(0x01)
    
    return


def PROCESS_CMD(pre, LD_funct, SA_funct, EXT_LD_FUNCT, EXT_SA_FUNCT):                                           # Processes 'B' (BASIC) commands sent by the TS
    
    global TSP
    global MQ
    
    global files
    
    TSP.zx48 = False
    cur_fname = TSP.f_name
    
    wrt = MQ.put
    cmd = bytearray(100)
    
    load_cmd = pre[1]
    
    long = pre[7] + 256*pre[8] + 3
    rl = range(long)
    
    wrt(0x40)
    wrt(0x01)
    
    for l in rl:
        cmd[l] = MQ.get()
    
    try:
        cmd = cmd[:long].decode()
    except:
        LOG("ERROR: Unrecognized string in PROCESS_CMD: FIFO Status:" + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 0)
        return

    cmd_exec = cmd[3:].upper()
    rest_cmd = cmd[7:]

    gc.collect()

    if load_cmd:                                                                                    # Is it a "LOAD:tpi:..." command.....?
        if cmd_exec in  LD_funct:                                                                   # is it valid? i.e. exists in the dictionary?
            EXEC = LD_funct[cmd_exec]
            EXEC()
            ACTIVATE_MQ()
            
        elif cmd_exec in  EXT_LD_FUNCT:                                                           # Is it an external cmd?
            EXEC = EXT_LD_FUNCT[cmd_exec]
            EXEC(pre, cmd)

        elif rest_cmd[0] == '*':                                                                    # Is it a shortcut (LOAD "tpi:*nn")

            try:
                index = int(rest_cmd[1:])
            except:
                index = 1000
                
            if files[index]:
                SEND_MSG("Mounting file: " + files[index], "", 1)
                TSP.f_name = TSP.cur_path + "/" + files[index]
                MOUNT_FILE()
                ACTIVATE_MQ()

            else:
                SEND_MSG("Index mount error: " + str(index), "", 3)
                
        elif rest_cmd == "dirinfo.tap":
            TSP.f_name = TSP.cur_path + "/" + "dirinfo.tap"
            MOUNT_FILE()
            ACTIVATE_MQ()
            SEND_MSG("Mounting dir info: ", rest_cmd, 1)
            
        elif rest_cmd in files:                                                                                  # Is rest_cmd a valid file? 
            TSP.f_name = TSP.cur_path + "/" + rest_cmd
            MOUNT_FILE()
            ACTIVATE_MQ()
            SEND_MSG("Mounting file: ", rest_cmd, 1)
            
        elif rest_cmd[-4:].upper() == ".TAP":
            TSP.f_name = TSP.cur_path + "/" + rest_cmd
            SEND_MSG("Mounting file: ", rest_cmd, 1)
        
        else:
            SEND_MSG('Error! Invalid LOAD "tpi:"', rest_cmd, 5)                                       # If none of the above, raise error
            LOG("ERROR: File does not exist in LOAD", 2)
            
    else:                                                                                                 # ...or it's a "SAVE:tpi:..." command
        if cmd_exec[:7] in SA_funct:                                                                      # Is valid, i.e. exists in dictionary?
            cmd_exec = cmd_exec[:7]
            EXEC = SA_funct[cmd_exec]
            EXEC(pre, cmd)
            
        elif cmd_exec in  SA_funct:                                                                               # Again, is a valid function? 
            EXEC = SA_funct[cmd_exec]
            EXEC(pre, cmd)
            
#         elif cmd_exec == "TPI:TEST":                                                                               # Remove in production!!!
#             
#             MQ.put(0x40)
#             MQ.put(0x01)
#             
#             for i in range(10):
#                 print(MQ.get())

        elif cmd_exec in EXT_SA_FUNCT:                                                                                # Is an external cmd?
            EXEC = EXT_SA_FUNCT[cmd_exec]
            EXEC(pre, cmd)
            
        else:
            SEND_MSG("Unrecognized command: " + cmd_exec,'SAVE "tpi:gethelp" for info', 5)                                                      # If none of the above, raise error
            LOG("ERROR: Unrecognized command: " + cmd_exec, 2)
    
    while(MQ.tx_fifo() != 0):
        pass
    
    while MQ.rx_fifo() != 0:
        fff = MQ.get()
        
    LOG("INFO: Exiting CMD processing: " + cmd_exec + " " + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 0)
    
    return


######################
# MAIN LOOP ROUTINES #
######################


def TS2068_IO():                                                         # Main IO loop, for SAVE, LOAD and commands processing
    
    global busy                                                        # whether 2nd core is busy
    global dead                                                        # boolean to indicate whether an IO routine is "alive" or not. Used for watchdog CHK_STATUS
    global files                                                       # array of only the files of current directory; used for index mounting of files ( LOAD "TPI:*nn") 
    global kill                                                        # boolean set to True when watchdog wants to end a misbehaving IO routine 
    global lista                                                       # all contents of current dir, in string format to be displayed by "TPI:DIR"
    global log_entries                                                 # log entries to be saved during next loop
    
    global ROM
    global BANK
    global MQ

    global led
    global TSP
    
    busy = False
    dead = True
    kill = False
    files = []
    lista = ""
    log_entries = ""
    led = Pin(25, Pin.OUT)

    init_values = LOAD_CONFIG()
    TSP = PICO_STATUS(init_values)
    
    try:
        log_len = os.stat("/activity.log")[6]
    except:
        log_len = 0
        
    if log_len >= 64_000:                                            # If log >= 64K generate a new log file
        
        try:
            os.remove("/activity.old")
        except:
            pass
        
        os.rename("/activity.log", "/activity.old")
        LOG("INFO: Starting new log file", 3)
    
    LOG("INFO: Starting TS Pico. Memory at startup: " + str(gc.mem_free()), 0)
    SAVE_LOG()
        

#     Uncomment the following two lines, for DCK *AND* ROM mapping
    ROM = StateMachine(4, set_ctrl, freq=150_000_000, in_base=Pin(0, Pin.IN), jmp_pin=Pin(26), set_base=Pin(21, Pin.OUT), out_base=Pin(19, Pin.OUT))
    ROM.active(1)

#     Uncomment the following two lines, for DCK access and no ROM mapping
#     ROM = StateMachine(4, set_dck, freq=150_000_000, jmp_pin=Pin(26), out_base=Pin(19, Pin.OUT))
#     ROM.active(1)

    BANK = StateMachine(5, sel_bank, freq=150_000_000, jmp_pin=Pin(26), out_base=Pin(15, Pin.OUT))
    BANK.active(1)

    ROM.put(TSP.ROM_SM)
    BANK.put(TSP.bank_sm)
    
    REMOVE_DIR("/TMP")
    os.mkdir("/TMP")
    
    os.chdir('/')
    
    LD_funct = {
        "TPI:DIR": DIR,
        "TPI:PATH" : PATH,
        "TPI:TAPDIR" : TAPDIR,
        "TPI:CONFIG" : LD_NOT_IMP,
        "TPI:LIST" : LD_NOT_IMP,
        }
    
    SA_funct = {
        "TPI:APPEND" : APPEND,
        "TPI:BLKRCV" : BLKRCV,
        "TPI:CD " : CDIR,
        "TPI:CLOSE": UNMOUNT,
        "TPI:FFW" : FWD,
        "TPI:GETHELP" : GETHELP,
        "TPI:GETINFO" : GETINFO,
        "TPI:GETLOG" : GETLOG, 
        "TPI:MD " : MDIR,
        "TPI:MEMBOOT" : MEMBOOT,
        "TPI:MEMDOCK" : MEMDOCK,
        "TPI:REW" : REW,
        "TPI:RM " : RMDIR, 
        "TPI:VERBOSE" : VERB_TOGGLE, 
        "TPI:ZX48" : ZX48,
        "TPI:AUTOLF" : SA_NOT_IMP,
        "TPI:AUTOPG" : SA_NOT_IMP,
        "TPI:BMP" : SA_NOT_IMP,
        "TPI:CLPRINT" : SA_NOT_IMP,
        "TPI:CONFIG" : SA_NOT_IMP,
        "TPI:DELETE" : SA_NOT_IMP,
        "TPI:FRESET" : SA_NOT_IMP,
        "TPI:GETCONFIG" : SA_NOT_IMP, 
        "TPI:MEMINFO" : SA_NOT_IMP,
        "TPI:NOAUTOLF" : SA_NOT_IMP,
        "TPI:OPPRINT" : SA_NOT_IMP,
        "TPI:PRNSZ" : SA_NOT_IMP,
        "TPI:STOP" : SA_NOT_IMP,
        }
    
    # Placeholders for External LD/SA commands
    
    EXT_LD_FUNCT = {
    
    }

    EXT_SA_FUNCT = {
    
    }

    dead = False
    _thread.start_new_thread(BLINK_LED, (0.9, ))
    
    LOG("INFO: Mounting SD Card...", 0)
    SAVE_LOG()

    ACTIVATE_SD()
    
    dead = True
    
    while busy:
        pass
    
    PERFORM_UPDATE()
    
    os.chdir(TSP.cur_path)
    DIR_FILES()
    
    os.umount("/sd")
    
    ACTIVATE_MQ()
    
    LOG("INFO: SD Card initialized and mounted OK", 0)
    SAVE_LOG()
    
    wrt = MQ.put
    
    LOG("INFO: TS Pico initialized OK. Waiting for commands...", 0)
    SAVE_LOG()
    
    led.value(0)

    pre = bytearray(10)
    r1 = range(10)

    ts = time.ticks_us()                                                                           # ts -> timestamp
    
    while True:                                                                                    # main execution loop

        if (MQ.rx_fifo()) != 0:
            
            ts = time.ticks_us()                                                                   # reset timestamp
            
            wrt(0x01)
            for i in r1:
                pre[i] = MQ.get()
                                                                                                      # pre(header)[0] is a command
            if pre[0] == 0 and pre[1] == 0:                                                           # pre[1] specifies which: if 0 -> SAVE   
                LOG("INFO: Starting SAVE TS", 0)
                
                led.value(1)
                
                while busy:
                    pass
                
                MQ, TSP, new_logs = SAVE_TS(MQ, TSP)
                log_entries += new_logs
                
                DIR_FILES()
                
                try:
                    os.umount("/sd")
                    ACTIVATE_MQ()
                    
                except:
                    pass
                
                led.value(0)
                
            elif (pre[0] == 0 or pre[0] == 255) and pre[1] < 10:                                      # for simplicity if 0 < pre[1] < 10: call LOAD routine 
                LOG("INFO: Starting TS LVM", 0)
                
                while busy:
                    pass
                MQ, TSP, new_logs = LOAD_TS(pre, MQ, TSP)
                log_entries += new_logs
                
            elif (pre[0] == 0 or pre[0] == 255):                                                      # Headerless LOAD
                LOG("INFO: Starting TS LVM - Headerless LOAD", 0)
                
                while busy:
                    pass
                MQ, TSP, new_logs = LOAD_TS(pre, MQ, TSP)
                log_entries += new_logs
                
            elif pre[0] == 66 and pre[1] == 5:                                                        # commands are pre[0] == 66. PRINT commands are pre[1] == 5
                LOG("INFO: Starting PRINT", 0)
                PRINT_IO(pre)
                DIR_FILES()
                
            elif pre[0] == 66:
                LOG("INFO: Starting TS COMMAND " + str(pre), 0)
                
                try:
                    PROCESS_CMD(pre, LD_funct, SA_funct, EXT_LD_FUNCT, EXT_SA_FUNCT)
                except:
                    LOG("ERROR: Invalid data received from PROCESS_CMD", 2)
                    break
                
                if TSP.zx48:
                    ZX48_IO()
                    
            elif pre[0] == 65:
                LOG('INFO: Starting "A" COMMAND', 0)
                
                PROCESS_ASM(pre)
                DIR_FILES()
                
            else:
                try:
                    LOG("WARNING: Unrecognized command! " +  pre, 1)
                except:
                    LOG("WARNING: Unrecognized command! Cannot get pre[] data", 1)
                
                while MQ.rx_fifo() != 0:
                    MQ.get()
                while MQ.tx_fifo() != 0:
                    MQ.exec("pull (noblock)")
                    MQ.exec("set (osr, null)")
                MQ.active(0)
                utime.sleep(.01)
                MQ.active(1)
                
                BLINK_ERROR()
                
                LOG("INFO: Cleared TX/RX FIFO after unrecognized cmd: " + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 0)
                
        else:
            if time.ticks_us() - ts < 2_000_000:
                continue
            elif time.ticks_us() - ts < 2_100_000:
                led.value(1)
            else:
                if log_entries:
                    if not busy:
                        _thread.start_new_thread(SAVE_LOG, ())
    
                led.value(0)
                ts = time.ticks_us()
                

def ZX48_IO():                                                                      # Main IO loop, for SAVE, LOAD and commands processing
                                                                                    # ZX Spectrum mode
    global MQ                                                                                    
    global TSP
    global log_entries
    global led
    
    led.value(0)
    
    MQ = StateMachine(0, TS_IO, freq=15_000_000, out_base=Pin(2, Pin.OUT), in_base=Pin(2, Pin.IN), jmp_pin=Pin(11), sideset_base=Pin(12, Pin.OUT))
    MQ.active(0)
    
    utime.sleep(0.01)
    MQ.active(1)
    
    LOG("INFO: Starting ZX Mode...", 0)

    ts = time.ticks_us()
    
    while True:
        
        if (MQ.rx_fifo()) != 0:
            
            ts = time.ticks_us()
            a = MQ.get()
            
            if a == 76:                                                    # ASCII 'L' - for LOAD

# uncomment these lines for 'regular' ZX Spectrum LOAD

                LOG("INFO: Starting ZX LOAD", 0)
                MQ, TSP, new_logs = LOAD_ZX(MQ, TSP)
                
# uncomment these lines for compatible-mode ZX Spectrum LOAD

#                 buf_size = 52100                                          # lower this if mem allocation error arises
#                 MQ, TSP, new_logs = LOAD_ZX_C(MQ, TSP, buf_size)
#                 log_entries += new_logs
                
            elif a == 83:                                                  # ASCII 'S' - for SAVE
                
                LOG("INFO: Starting ZX SAVE", 0)
                MQ, TSP, new_logs = SAVE_ZX(MQ, TSP)
                log_entries += new_logs
                      
            elif a == 100:                                                  # ASCII 'X' - for EXIT. David, change this to whatever you thing suits better
                LOG("INFO: Ending ZX mode. Free mem: " + str(gc.mem_free()) + ". Returning to TS processing.", 0)
                gc.collect()
                
                break
            
            else:
                LOG("WARNING: Unrecognized ZX command", 0)
                while MQ.rx_fifo() != 0:
                    MQ.get()
                while MQ.tx_fifo() != 0:
                    MQ.exec("pull (noblock)")
                    MQ.exec("set (osr, null)")
                MQ.active(0)
                utime.sleep(.01)
                MQ.active(1)
                
                LOG("INFO: Cleared TX/RX FIFO after unrecognized ZX command: " + str(MQ.tx_fifo()) + " " + str(MQ.rx_fifo()), 0)

        else:
            if time.ticks_us() - ts < 2_000_000:
                continue
            elif time.ticks_us() - ts < 2_100_000:
                led.value(1)
            else:
                
                if log_entries:
                    SAVE_LOG()
                    log_entries = ""
                    
                led.value(0)
                ts = time.ticks_us()
