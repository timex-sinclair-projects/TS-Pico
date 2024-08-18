# Commands

The TS-Pico implements its commands through the Timex/Sinclair's LOAD and SAVE commands.

### Testing the commands
Each command listed below includes a description of what the command does and expected output/feedback to the user.

They also have a **How to test** section. Follow these directions precisely. They document the normal and expected uses of the command.

#### Breaking the commands

Once you've established that the command performs as expected (or not: remember, report it as an issue), try the same commands with different values. Try:
- no *filename* where one is expected
- a *filename* (or string of characters) where one is not expected
- a *filename* that exceeds 10 characters
- a *filename* with non-alphanumeric characters
- the command in a program
- breaking out of the command mid-stream (shift+spacebar), before the TS-Pico has completed its operations
- a canary (I don't know how you'll stuff a canary in the computer; canary not supplied)

Use your imagination, use fat fingers to "mess up" a command... try the most outrageous idea you can imagine for the command.

In short: break the TS-Pico.

---

## LOAD Commands

### LOAD "tpi:*filename.tap*"
Mount a TAP file 

#### LOAD "tpi:*filename.dck*" ![New-PNG-HD](https://github.com/user-attachments/assets/2efc94ff-667d-47a8-98bd-3ce2ad18776b)

LOAD "" will load a special program will ask you a few questions about whether to save the DCK image on Static RAM or Flash and which of the available slots.

If you indicate that you want to keep the configuration, the Pico will reset and use the image you've loaded as a mounted DCK; otherwise you'll need to issue SAVE "tpi:memdock" CODE nn,mm to activate, with nn=1 to use the SRAM, nn=2 use the Flash, and mm an even number between 0 and 14 to select the slot. Any other values will result in error. Also, notice currently the TS-Pico doesn't validate whether there was a previous DCK image in the selected slot; actually, the selected slot gets wiped out prior to writing the image. Use with caution. As a security measure, you cannot write anything (DCK or ROM) on slots 0 and 1 on the Flash. It is advisable to use SRAM whenever possible; Flash should only be used to store images between reboots.

From this moment on, the image will act exactly as if a physical cartridge is inserted on the slot. Some cartridges must be activated via OUT 244, 3; some others just need a NEW command, and even some others need a physical reset to start.

#### LOAD "TPI:*nn"
Loads a TAP file based on the index number.

#### LOAD "tpi:*filename.rom*" 
LOAD "" will load a special program will ask you a few questions about whether to save the ROM image on Static RAM or Flash and which of the available slots.

Unlike with DCKs, you must manually select the newly saved ROM to be active. Type SAVE "tpi:memboot" CODE nn,mm again with nn=1 to use the SRAM, nn=2 use the Flash. This time, mm can be any number  between 0 and 15. Again, it is better to use the SRAM instead of the Flash, unlike you want to keep the image between reboots. Same restrictions as the DCK image apply; you cannot use Flash slots 0 and 1

Also, notice that in some very limited cases, as the ROM is switched on-the-fly, depending on the cycle the processor is caught when switching the ROM, the TS could hang. If this happens, just reset. The Pico will reset as well, and use the newly switched ROM. But in the next cycle, the TS will revert to stock ROM, to prevent the system from not booting at all if the ROM is corrupted. This should be configured as a startup parameter.

#### LOAD "tpi:*filename.bin*"
This command will mount a binary file on the Pico internal flash, and have it ready for streaming to the TS with the command SAVE "tpi:blckreceive" CODE nn,mm (see below).

### LOAD "tpi:dir"
Get a listing of the current directory

### LOAD "tpi:tapdir"
Get a listing of the files in the mounted TAP file

---

## SAVE Commands

### SAVE "*filename*"
Creates a new TAP file called *filename*.tap.

#### How to test
1. Start at the power-on state
2. Enter a short program
3. SAVE "*filename*"
4. LOAD "tpi:dir" to confirm the file exists
5. LOAD "tpi:*filename*.tap" to mount the file
6. LOAD "" to load the first file in the TAP file

### SAVE "TPI:APPEND"
Enable append to mounted TAP file. Instead of SAVE "*filename*" creating a new TAP file, *filename* will be appended to the currently mounted TAP file. IF no file is mounted, an error occurs

#### How to test
1. Start at the power-on state
2. LOAD "tpi:*filename*.tap" to mount a TAP file (I suggest you use the same one you created with the SAVE command, above)
3. LOAD "" to load the first file in the TAP file
4. Add a new line or two to the program
5. SAVE "tpi:append"
6. SAVE "*newfilename*"
7. LOAD "tpi:tapdir" to list the files in the TAP file
8. Add a few more lines to the current program
9. SAVE "*filename3*" (a unique filename)
10. LOAD "tpi:tapdir" to list the files in the TAP file

### SAVE "TPI:BLKRCV" [CODE nn,mm]
Stream to the TS a binary file, previously mounted with LOAD "tpi:*filename.bin*". As an example, generate a small file (100-200 bytes) with known content, name it as *something.bin*, and then execute this small program:

10 LOAD "tpi:*something.bin*"

20 SAVE "tpi:blkrvc"

30 FOR i=1 TO 100 (or the known file size) 

40 PRINT IN 14; " ";

50 NEXT i

You should see the values contained in the file. Notice you MUST consume all of the bytes for the Pico to resume normal operation; otherwise the queue will be full and will disrupt further operation. There's no way of recovering from this error, as the TS-Pico will wait indefinitely to stream the remaining bytes. Only workaround is that caare must be taken to ensure all bytes are consumed.

CODE nn,mm indicates "send nn bytes, starting from offset mm". CODE 0, m and CODE n, 0 are all valid. If the combination of parameters results in sending an amount of bytes that is larger than the file size, an error occurs.

This command is intended as an auxiliary command to implement further functions in a BASIC program.


### SAVE "TPI:CD *<dirname>*"
Change to named directory

### SAVE "TPI:CLOSE"
Unmount a mounted TAP file

### SAVE "TPI:FFW"
Move the internal file pointer to the next block in the TAP file
Moves pointer to next block in TAP file; also can skip 'CODE n' # of blocks forward

### SAVE "TPI:GETHELP"
Lists the available commands.

### SAVE "TPI:GETINFO"
Shows TS-Pico internal status

### SAVE "TPI:GETLOG" CODE nn, 0
Shows the last nn bytes of the activity.log file

### SAVE "TPI:MD *<dirname>*"
MAKE DIRectory in the current path.

### SAVE "TPI:MEMBOOT" CODE nn, mm
Changes ROM slot to boot from (mm=0..15); either SRAM (nn=1) or Flash (nn=2)

### SAVE "TPI:MEMDOCK"
Changes DCK slot (mm=even [0..14] either SRAM (nn=1) or Flash (nn=2)

### SAVE "TPI:REW"
Moves pointer to next block in TAP file; also can skip 'CODE n' # of blocks backwards

### SAVE "TPI:RM *<dirname>*"
Removes the named directory. No confirmation asked (to be implemented). Use with caution.

### SAVE "TPI:VERBOSE"
Toggle command feedback verbosity ON/OFF. Might disrupt BASIC programs if enabled.

### SAVE "TPI:ZX48" - ZX48
Changes to ZX Spectrum 48 compatability mode.

## Commands not yet implemented
The following commands are on the to-do list. You're welcome to jump in and help implement them. :)
- LOAD "tpi:config"
- LOAD "tpi:list"
- SAVE "TPI:AUTOLF"
- SAVE "TPI:AUTOPG"
- SAVE "TPI:BMP"
- SAVE "TPI:CLPRINT"
- SAVE "TPI:CONFIG"
- SAVE "TPI:DELETE"
- SAVE "TPI:FRESET"
- SAVE "TPI:GETCONFIG"
- SAVE "TPI:MEMINFO"
- SAVE "TPI:NOAUTOLF"
- SAVE "TPI:OPPRINT"
- SAVE "TPI:PRNSZ"
- SAVE "TPI:STOP"
