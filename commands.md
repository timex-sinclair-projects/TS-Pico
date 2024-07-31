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

### SAVE "TPI:APPEND"
Enable append to mounted TAP file
Start appending each newly SAVEd file to currently mounted TAP

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
