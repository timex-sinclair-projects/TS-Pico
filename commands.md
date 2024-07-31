# Commands

The TS-Pico implements its commands through the Timex/Sinclair's LOAD and SAVE commands.

## LOAD Commands

### LOAD "TPI:*filename.tap*"
Mount a TAP file 

### LOAD "tpi:dir"
Get a listing of the current directory

### LOAD "tpi:tapdir"
Get a listing of the files in the mounted TAP file

### LOAD "tpi:config"
Not implemented

### LOAD "tpi:list"
Not implemented

## SAVE Commands

### SAVE "*filename*"
Creates a new TAP file called *filename*.tap.

#### How to test
1. Start at the power-on state
2. Enter a short program
3. SAVE "*progname*"
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

### SAVE "TPI:AUTOLF"
Not implemented

### SAVE "TPI:AUTOPG"
Not implemented

### SAVE "TPI:BMP"
Not implemented

### SAVE "TPI:CLPRINT"
Not implemented

### SAVE "TPI:CONFIG"
Not implemented

### SAVE "TPI:DELETE"
Not implemented

### SAVE "TPI:FRESET"
Not implemented

### SAVE "TPI:GETCONFIG"
Not implemented

### SAVE "TPI:MEMINFO"
Not implemented

### SAVE "TPI:NOAUTOLF"
Not implemented

### SAVE "TPI:OPPRINT"
Not implemented

### SAVE "TPI:PRNSZ"
Not implemented

### SAVE "TPI:STOP"
Not implemented
