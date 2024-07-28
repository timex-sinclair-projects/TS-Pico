# Guidelines for testing TS-Pico v1.1 Beta

# Update process
   Start with a stock v1.0 TS-Pico with the file structure detailed in ```/src_old_v1.0``` and with firmware ```/stock_firmware_v1.0.uf2``` flashed. Replicate the ```/UPD``` folder in the root of SD Card, and flash the Pico with the
 ```/new_firmware_v1.1.uf2```. At the end a successful update process, see if you get the files as in ```/src_new_v1.1```, both in content and structure. Pay attention to the Pico LED flashing sequences: start with some random, fast blinking, and after a couple of seconds, the flashing pattern will be either fast blinking (indicating an error) or slow blinking (all was good). Examine the log entries in ```/activity.log``` to see either successful or failed messages. Check that the ```/UPD``` was successfully erased at the end of the process, no matter the result. Take note of the possible errors that arise  

# Basics: SAVE/LOAD/VERIFY/MERGE
The SLVM routines have been optimized, should work better than before. Try them with your preferred .TAP files, see if there's one in particular that does something off. Try the SAVE with the new APPEND feature (see the new commands). Report anything unusual. Pay attention to the auto-rewind feature, by which once a TAP file is LOADed, its pointer returns to the beginning. Try the FWD and REW to see if they work as expected.

Some of the optimizations/fixes in SLVM include: 

- LOAD routine now validates block type, to avoid error on LOAD "" CODE for a BASIC pgm for instance
- Append newly SAVEd file to currently mounted TAP (if  ```SAVE "tpi:append``` is enable, of course)
- Fixed small errors on mounting file and tap_idx references. Now mounting an already mounted file (remounting?) behaves correctly, i.e. goes to the first block of the TAP
- Fixed LOADing non-existent filename from .TAP. i.e.  ```LOAD "foo"``` from a mounted .TAP that doesn't have that filename will cycle on all the headers on the .TAP until stopped with BREAK 
- Fixed special characters and trailing spaces in filename SAVE
- Incorrect commands now show description of error (if ```SAVE "tpi:verbose``` is enable)
- Two consecutives LOAD "" with no file mounted is now properly handled (i.e. ```LOAD ""``` then ```LOAD ""``` and no file mounted
- TAP loop around now works 
- Nonexistent/nonworking SD Card is now reported on the log and the TS-Pico is halted, with info appened to the ```activity.log``` file


# New status and troubleshooting tools
A few commands have been added that should enable for more thoroughful testing and user information; these are:

```"TPI:GETHELP"```

```"TPI:GETINFO"```

```"TPI:GETLOG"```

```"TPI:VERBOSE"```

Each is self-explanatory, starting from the first one. Try them whenever you find something unusual or off. Provide this info when reporting an error.


# Save .DCK and .ROM images to Flash/SRAM
   Check that a ```LOAD "tpi:dir"``` now display also .DCK, .ROM  and .BIN files (also verify the listing is now in alphabetical order). Try to mount, say, a .DCK with the regular ```LOAD "tpi:file.dck"``` or ```LOAD "tpi:*nn"``` for shortcut mode (you can find a selection of DCK and ROM images in the proper location of the GitHub repository for Beta Testing). After the file is mounted, do a ```LOAD ""``` as usual. A program called ```dckupdate``` should automatically start, with guidelines as to where (slot of the Flash/SRAM) to store the DCK. After the warnings, it should perform the update of the .DCK to the desired location. The program finishes asking whether you want to use this new location as a .DCK or not; choose the one you like. The program finishes with rebooting, after which, if automatically selected, the program on the DCK should start; if no auto-selected, make the appropiate selection with ```SAVE "tpi:memdock CODE n, m```, where n is the Flash (01) or SRAM (02) and m is the slot where the DCK is located (even 0..14). Remember that some DCKs must be activated via ```OUT 244, 3```, for instance the Spectrum ROM cartridge. Check that the dock works as expected

   The same procedure can be used to update the Flash/SRAM with a new ROM; this time a program called ```romupdate``` will start (notice that both ```dckupdate.tap``` and ```romupdate.tap``` are part of the UPD folder, and now should be located on the ```/TAP``` folder of the Pico internal Flash filesystem). The program will ask for a slot (4..14) of the Flash (01) or SRAM (02) to store the new ROM, and complain if stored in 0..3, but will do so, WITH THE EXCEPTION of slot 1 of Flash; this contains the system ROM and cannot (should not) be updatable. The ROM cannot be automatically selected in the program, you need to finish, reboot and select the appropiate ROM image via ```SAVE "tpi:memboot CODE n, m```. n and m are exactly the same as in the DCK operation, with the exception that now all slots are available from 0 to 14 for selection.

   After ```SAVE "tpi:memboot CODE n, m``` the selected ROM should start immediately, if not do a hard reset. The ROM will start once, then after reboot a second time, and the third time the system will reboot with the stock TS 2068/ TS-Pico ROM. This is by design as a way out in case of a failed ROM get stuck. 
 
 Check several DCKs and ROMs, see if they work as expected. Some DCKs work in SRAM and not in Flash, other the opposite. Still trying to figure out why.

# New Spectrum ROM is needed
As a by-product of the previous, a new Spectrum image is needed for compatibility with this version; previous Spectrum version won't work. Look for the new version on the proper folder, and try upgrading the ROM image on slot 0 of the Flash with the correct version. See if the Spectrum ROMs now LOAD and SAVE properly. 

# New Spectrum compatibility mode
Some Spectrum ROMs won't work in Spectrum mode with the standard LOAD routine (most noticeably the "White Jaguar" game) so a new, compatible-mode was developed. You'll find how to enable this compatible mode routine in lines 2001-2010 of ```tspico.py``` script. In order to use it, you'll have to also change the import sentence on the ```main.py``` script on the Pico, using Thonny, https://viper-ide.org/ or any IDE you choose 

# Test Ryan's optimization
A problem occurs when, within a running program, one tries to LOAD "" a non-autostart program. This version of the ROM corrects this. Try if this works with your programs (Ryan Gray noticed this, and proposed a fix)  

# ```dirinfo.tap```
A hidden .TAP file is created when navigating thru directories. This file can be accessed programatically with ```LOAD "tpi:dirinfo.tap" DATA a$()```. This will create a vector of 32 characters alphanumerical strings.The first and second elements are actually numbers, that can be read with ```LET n=VAL(a$(1))``` for example. First number is the number of directories in the current folder (let's call it ```n```), the second is the number of files (or ```m```). Starting from the third element, you will find the names of the ```n``` folders existing in the current directory, followed by the ```m``` files in it. So, the ```a$()``` matrix will have a total of n+m+2 elements, each an array of 32 positions. Either ```n, m``` or both can be 0. Each string will have the full name if it's a directory, or a concatenation of: a 3 numbers index, the first characters of the name, and the size of the file. This info can be parsed into a BASIC program for file management, for example.

Try to LOAD this file from your BASIC program, using differents folders, see if the contents match with what's reported in ```LOAD "tpi:dir"``` for instance.

# Test the new commands
This is the list of the new supported commands, all of them are ```SAVE "tpi:..."``` commands:

```"TPI:APPEND"```

```"TPI:BLKRCV"```

```"TPI:MEMBOOT"```

```"TPI:MEMDOCK"```


See if they perform as expected, if the output and behaviour are consistent. 


# For the adventurous....
Not specifically Beta Testing, but for people who want to modify the ```tspico.py``` script, here a couple guidelines:

- Start by studying the Pico schematics; try to see how all the components act together. This will come in handy when understanding, for instance, the StateMachines, the working of the Flash, SRAM, SD Card, I/O, etc. Pay a good look at that info
- Take a look at ```main.py```, see where the main loop function ```TS2068_IO``` is imported. Take a look at the other parts of the program, how ```activity.log``` is updated for instance
- Look how ```tspico.py``` is structured. See the four groups of functions: SERVICE FUNCTIONS, LOAD CMD FUNCTIONS, SAVE CMD FUNCTIONS, and MAIN LOOP FUNCTIONS.
- Study the pre-header: fields, meaning, behaviour
- Pay special attention to these functions: ```SEND_MSG, SEND_MSG2, TS2068_IO, ZX48_IO, PROCESS_CMD```
- Also, pay attention at the ```LD_funct``` and ```SA_funct``` functions dictionaries. See also the placeholders where EXT_CMDs can be implemented
- Finally, take a look at the "work-in-progress" functions: ```PRINT_IO``` and ```PROCESS_ASM``` functions





