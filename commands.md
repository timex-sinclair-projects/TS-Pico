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

## LOAD Commands

### LOAD "tpi:*filename.tap*"
Mount a TAP file 

#### LOAD "tpi:*filename.dck*"
LOAD "" will load a special program will ask you a few questions about whether to save on Static RAM or Flash and which of the available slots.

If you indicate that you want to keep the configuration, the Pico will reset and use the file you've loaded.

#### LOAD "TPI:*nn"
Loads a TAP file based on the index number.

#### LOAD "tpi:*filename.rom*" or LOAD "tpi:*filename.bin*"
LOAD "" will load a special program will ask you a few questions about whether to save on Static RAM or Flash and which of the available slots.

### LOAD "tpi:dir"
Get a listing of the current directory

### LOAD "tpi:tapdir"
Get a listing of the files in the mounted TAP file

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
Enable append to mounted TAP file. Instead of SAVE "*filename*" creating a new TAP file, *filename* will be appended to the currently mounted TAP file.

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

### SAVE "TPI:BLKRCV" [CODE n,m]
'Internal' command to send block to be written to Flash.

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

### SAVE "TPI:GETLOG"
Shows the last nn bytes of the activity.log file

### SAVE "TPI:MD *<dirname>*"
MAKE DIRectory in the current path.

### SAVE "TPI:MEMBOOT"
Changes ROM slot to boot from; either SRAM or Flash

### SAVE "TPI:MEMDOCK"
Changes DCK slot; either SRAM or Flash

### SAVE "TPI:REW"
Moves pointer to next block in TAP file; also can skip 'CODE n' # of blocks backwards

### SAVE "TPI:RM *<dirname>*"
Removes the named directory.

### SAVE "TPI:VERBOSE"
Toggle command feedback verbosity ON/OFF.

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
