import os
import time
import json
import sys

from sdcard import *
from machine import Pin, freq, SPI
from gc import collect, mem_free


def FINISH(msg, log_ena, success):                                                        # Logs the final status msg, and blinks LED at different intervals, to indicate either success or fail
                                                                                          # msg=text to be displayed/logged; log_ena=whether logging is enabled; success=boolean if status is ok or failed
    if success:
        interval = 0.8
    else:
        interval = 0.08
    
    led = Pin(25, Pin.OUT)
    
    if log_ena:
        LOG(msg)
        os.umount("/sd")
    else:
        print(msg)
    
    while True:
        led.toggle()
        time.sleep(interval)
        

def LOG(msg):                                                                           # Logs a message to upgrade.log and screen 

    with open("/sd/upgrade.log", "a") as log_file:
        log_file.write(msg + "\n")
        
    print(msg)
    
    return


def COPY_FILE(src, dst):                                                                # Copy file from src to dst, optimized with global buf and memoryview. Absolute path must be provided in src, dst

    global buf
    rd_bytes = 0

    f_in = open(src, "rb")
    f_out = open(dst, "wb")

    rd_bytes = f_in.readinto(buf)                                                        # rd_bytes: amount of bytes read

    while rd_bytes > 0:
        mv = memoryview(buf)                                                             # we use memoryview to avoid creating a new array with the slice
        f_out.write(mv[:rd_bytes])
        rd_bytes = f_in.readinto(buf)

    f_in.close()
    f_out.close()
    
    return


def RESTORE_FILES(src, dst):                                                             # Restores prev backed-up files; typically scr=/sd/BACKUP - dst = / (root of the Flash)

    if os.stat(src)[0] == 0x4000:
    
        for el in os.listdir(src):
            f_name = src + '/' + el
            
            if (dst == "/"):
                new_path = dst + el
            else:
                new_path = dst + '/' + el
                
            if os.stat(f_name)[0] == 0x4000:
                
                LOG("Restoring folder " + f_name)
                
                try:
                    os.mkdir(new_path)
                    LOG("RESTORE: folder " + new_path + " not found; succesfully created")
                except:
                    LOG("WARNING: Folder " + new_path + " already exists during RESTORE. Moving on")
                
                RESTORE_FILES(f_name, new_path)
            else:        
                LOG("Restoring file " + f_name + " to " +  new_path)
#                 COPY_FILE(f_name, new_path)


def REMOVE_DIR(d):                                                                        # Recursively remove provided "d" directory and all its contents
    
    try:
        if os.stat(d)[0] & 0x4000:  # Dir
            for f in os.ilistdir(d):
                if f[0] not in ('.', '..'):
                    REMOVE_DIR("/".join((d, f[0])))  # File or Dir
            os.rmdir(d)
            LOG("Directory " + d + " removed ok")
        else:  # File
            os.remove(d)
            LOG("File " + d + " removed ok")            
    except:
        LOG("WARNING: could not remove directory " + d)
    pass
        
    return


def BACKUP_DIR(d, dest_dir):                                                               # Recursively backs-up folders and files of a provided "d" folder; typically d="/" (root of the Flash)
                                                                                           # and dest_dir = /sd/BACKUP
    if os.stat(d)[0] & 0x4000:  # Dir
        
        copy_path = str(dest_dir) + str(d)
        
        if (copy_path == dest_dir + "/"):
            copy_path = dest_dir
            
        try:
            os.mkdir(copy_path)
        except:
            FINISH("Fatal error. Could not create folder " + copy_path + ". Verify SD Card contents. Terminating", True, False)
        
        for f in os.ilistdir(d):
            if f[0].startswith("sd"):
                continue
            
            if f[1] & 0x8000:
                copy_src = d + '/' + f[0]
                copy_dst = copy_path + '/' + f[0]
                LOG("Copying file " + copy_src + " to " + copy_dst)
                
                COPY_FILE(copy_src, copy_dst)
                continue
            
            if f[0] not in ('.', '..'):
                folder_name = d + '/' + f[0]
                LOG("Processing folder " + folder_name)
                BACKUP_DIR(folder_name, dest_dir)  # File or Dir
        
    return


def TS2068_IO():                                                                           # Main executive routine; named like the one in tspico.py

    global buf                                                                             # global buffer to be used by COPY_FILE
    buf = bytearray(32768)

    led = Pin(25, Pin.OUT)
    U6_EN = Pin(12, Pin.OUT, Pin.PULL_UP)                                   # We disable U6_ENABLE, just in case.....

    log_ena = False                                                         # boolean; whether we've enabled logging to file or not

    last_run = {}                                                           # dictionary to hold last upgrade run's status
    init_values = {}                                                        # dictionary of current config.ini values
    new_values = {}                                                         # dictionary of upgrade config.ini values
    upgrade_dict = {}                                                       # dictionary of files to be upgraded

    U6_EN.value(1)

    U3_CS       = Pin(28, Pin.OUT, Pin.PULL_UP)                             # SD Card initialization
    D0          = Pin(2,  Pin.IN)
    D1          = Pin(3,  Pin.IN)
    D2          = Pin(4,  Pin.IN)
    
    for i in range(20):                                                     # We give the user 10s and 20 LED blinks to abort installation
        time.sleep(.5)
        led.toggle()

    led.value(1)

    print("TS Pico Upgrade setup (c) 2024 TS-Pico DevTeam")
    print("IMPORTANT!!!! DO *NOT* INTERRUPT THIS SEQUENCE!!!!")

    time.sleep(1)

    print("Mounting SD Card")

    try:

        spi = SPI(0, sck=D0, mosi=D1, miso=D2)
        sd = SDCard(spi, U3_CS)
        os.mount(sd, "/sd")
        
    except:
        
        FINISH("Fatal error. Could not mount SD Card. Terminating", log_ena, False)

    led.value(0)

    log_ena = True                                                           # start logging to upgrade.log
    
    LOG("====================================")
    LOG("TS-Pico Upgrade Setup initialized ok")
    LOG("SD Card mounted ok")

    try:
        with open("/sd/last_run.ini", "r") as f:                             # Try to determine last run's status
            last_run = json.load(f)
            last_run_status = last_run["status"]
    except:
        last_run_status = "None"

    LOG("Previous run status: " + last_run_status)

    try:
        os.chdir("/sd/UPGRADE")
    except:
        FINISH("Fatal error. Could not find UPGRADE folder on the SD Card. Terminating", log_ena, False)

    LOG("UPGRADE folder found in SD Card")

    if last_run_status == "BACKUP_PERFORMED":                                # If last run was unsuccessfull, but the backup creation wasn't, we restore that backup 
                                                                             # in case something went wrong last time
        LOG("Previous run was unsuccessful. Attempting to roll back...")
        
        try:
            RESTORE_FILES("/sd/BACKUP", "/")                                      # if so, restore backup
            LOG("System rolled back successfully. Continue with upgrade process")
            
        except Exception as err:
            LOG("System roll back failed. Reason: ")
            
            with open("/sd/upgrade.log", "a") as log:
                sys.print_exception(err, log)
            
            FINISH("Fatal error. Could not rollback system. ", log_ena, False)

    try:
        with open("/config.ini", "r") as f:                                  # try to load config values from config.ini file
            init_values = json.load(f)
    except:
        pass
            
    try:
        with open("/sd/UPGRADE/config.ini", "r") as f:                      # load values from config.ini file on the /sd/UPGRADE folder
            new_values = json.load(f)
    except:
        FINISH("Fatal error. Could not find config.ini file in UPGRADE folder. Terminating", log_ena, False)

    if not "FW_VERSION" in init_values:
        fw_version = "1.00"
    else:
        fw_version = init_values["FW_VERSION"]
            
    LOG("Current firmware version: " + fw_version)

    new_fw_version = new_values["FW_VERSION"]
    LOG("New firmware version: " + new_fw_version)

    if (fw_version == new_fw_version):
       FINISH("Current version is the same as upgrade. Nothing to do. Terminating", log_ena, True) 

    os.chdir("/sd")

    if "BACKUP" in os.listdir():
        
        LOG("Removing old BACKUP folder from previous run")
        
        try:
            REMOVE_DIR("/sd/BACKUP")
            LOG("Previous BACKUP folder removed")
        except:
            FINISH("Error removing previous backup folder. Terminating", log_ena, False)

    dest_dir = "/sd/BACKUP"

    LOG("Starting current firmware backup")

    led.toggle()
    time.sleep(.1)                                                      # Short LED blink = stage 1 completed ok (initialization)
    led.toggle()

    BACKUP_DIR("/", dest_dir)
    os.chdir("/")

    with open("/sd/last_run.ini", "w") as f:
        last_run["status"] = "BACKUP_PERFORMED"
        json.dump(last_run, f)

    LOG("Firmware backup finished ok")

    LOG("Processing new files")

    time.sleep(1)

    led.value(0)
    time.sleep(.1)
    led.toggle()
    time.sleep(.1)                                                      # Two short LED blinks = stage 2 completed ok (backup)
    led.toggle()
    time.sleep(.1)
    led.toggle()
    led.value(1)


    os.chdir("/sd/UPGRADE")
    
    with open("/sd/UPGRADE/upgrade.json", "r") as f:                                  # try to load config values from config.ini file
        upgrade_dict = json.load(f)
    
    
    for el in upgrade_dict["dirs"]:
        
        try:
            REMOVE_DIR(el)
        except:
            LOG("Warning: could not remove folder " + el + "; continue process...")         
            pass
        
        try:
            os.mkdir(el)
            
        except:                
            FINISH("Fatal error: unable to create folder " + el + " during Update. Terminating.", log_ena, False)
            
    for el in upgrade_dict:
        
        if el == "dirs":
            continue
        
        if el == "main.py":
            os.rename("/main.py", "/main.old")
            LOG("'main.py' renamed to 'main.old'")
            
        try:
            COPY_FILE(el, upgrade_dict[el]+el)
        except:
            FINISH("Fatal error: unable to copy file " + el + " during Update. Terminating", log_ena, False)

    os.remove("/main.old")
    LOG("'main.old' removed ok")

    with open("/sd/last_run.ini", "w") as f:
        last_run["status"] = "UPGRADE_PERFORMED"
        json.dump(last_run, f)

    try:
        new_folder = "/sd/BACKUP_FIRMWARE_V" + fw_version
        os.rename("/sd/BACKUP", new_folder)
    except:
        LOG("Error attempting to rename BACKUP folder; trying another name")
        
        try:
            num = str(len(os.listdir("/sd")) - 5)                                              # At this point, there are 6 elements on the '/' folder. So, subsequent BACKUP files 
            new_folder = "/sd/BACKUP_FIRMWARE_V" + fw_version + "[" + num + "]"                # will be named BACKUP_FIRMWARE_V1.1c[1], ....FIRMWARE_V1.1c[2], etc

            os.rename("/sd/BACKUP", new_folder)
            
        except:
            LOG("WARNING: Error renaming folder " + new_folder)
            
    LOG("Finished renaming BACKUP folder")

    FINISH("All process finished successfully. Check the upgrade.log file on the SD Card for more info", log_ena, True)

