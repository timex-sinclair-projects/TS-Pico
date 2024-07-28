# TS2068-PICO Beta-Testing branch


# WARNING!!! Remember to INSTALL the jumper on P10 (next to the Flash IC) on your TS-Pico board, or the write to the Flash/SRAM won´t work!

<img src="/P10_location.jpg" alt="Install this jumper" width="800"> 


This jumper comes by default open, so the /WR signal doesn´t reach either the Flash or SRAM. It needs to be enabled for the write to those memories is enabled.


# Intro

This branch is to be used for testing the new (and possibly upcoming) firmware updates. Files in this branch can be shared between beta testers **WITH THE EXCEPTION** of the files in the ```docker``` folder; specially the ```tspico_io.py``` file. It contains code that is either dangerous/inconvenient to fall into the wrong hands...enough said. The folder in general and the file in particular are only intended to be used to generate the firmware updates

# Folders structure:
```UPD```: This folder must be duplicated onto the SD to be read during update. The main component is a JSON file with all the new directories to be added, and also the files and its location. The files to be copied are also there; they include ```tspico.py``` itself, the main routine to be modified by the user; ```activity.log``` to store debugging error msgs, ```config.ini``` to store initial configuration values; and a couple ```.TAP``` files used by service routines

```docker```: discussed in the intro. Contents used to generate the firmware; namely a ```Dockerfile``` with definitions for Docker; personalized ```mpconfig.h``` (only the banner is modified); and the aforementioned ```tspico_io.py``` file 

```src_old_v1.0```: is the file structure of a "canonical" TS-Pico v1.0, as shipped, previous to upgrade. Useful to rebuild a stock Pico and re-try the update process. Also, the file ```old_firmware_v1.0.uf2``` can be found on the root for the same purposes

```src_new_v1.1```: contains the file structure of a "canonical" TS-Pico when updated from v1.0 to v1.1

Note that the ```tspico.py``` files located on all directories are exactly the same; however each has a different meaning 

# Usage:
A regular user (in this case our beta testers) would only need:
- the file ```new_firmware_v1.1.uf2``` located in the root of the ```Beta-Testing``` repository
- the folder ```UPD``` replicated on the root of the TS-Pico SD card

... and that's it! Hopefully, once the new firmware is flashed on via the ```BOOTSEL``` button on the Raspberry Pi Pico, the next boot should take it from there.

It is not necessary nor convenient that the TS-2068 is turned on during update; so better turn it off and even better, remove the TS-Pico from the socket for upgrade. Connect a USB cable to the Pico and the computer containing the firmware file. 

The upgrade will flash the LED on the Pico in a different way than usual; some short blinks and then the "process finished" blinking pattern: if successful, the LED will blink slowly; if there was any error the LED will blink fast. Aditional info will be found on the ```activity.log``` file located on the TS-Pico Flash filesystem root; this file can be opened with Thonny or a similar editor. 

 If we look at  ```main.py``` routine, it imports the main routine (```tspico.py```) from the firmware itself by default. If the user wants to modify existent routines, or add new ones, he/she must edit ```/TS/tspico.py``` and comment/uncomment the import sentence on ```main.py``` correspondingly. If something goes wrong, he/she can always import the original, unmodified routine from the firmware by simply comment/uncomment again.

I made every possible effort so the process is reversible; that is, if the upgrade process fails, the Pico can be reverted to its original state. Of course I can not provide guarantees for this, and should be one of the main things to be tested.

# Additional resources:
For more extensive beta testing, and for people who want to develop new routines, a couple more components are highly recommended:  

- A spare Pico will be of much help; or even better a whole new board.  
- ```Thonny``` and ```rshell``` installed on the system. The first is the most recommended IDE for the Raspberry Pi Pico, and the one I use. Any IDE can be used, however. David suggested https://viper-ide.org/ which I (still) didn't try, but looks promising! ```rshell``` is a very useful tool, mainly to back-up the whole Pico with a single command.
- For people developing new routines, Gustavo's extensive ROM documentation is a must. Otherwise, none of the messages exchange between the TS and the Pico makes any sense. Read the docs carefully! And make use of the author, who is always interested in sharing his extensive knowledge of the TS internals.

# ```tspico.py``` contents:
The file is just a large Python script, that imports the low-level functions from ```tspico_io.py``` but implements everything else in the script itself. There are four sections: Service Functions, LOAD Command Functions, SAVE Command Functions, and Main Loop Functions. Each section has functions alphabetically ordered. I made many comments and remarks on every funcion, and made all efforts for it to be readable and understanable; of course there's plenty of room for improvement in that area.

Finally, I left both a changelog and some functions to be implemented in future releases, so this can be done in a group effort

# To-Do:
- Add the DCKs and ROMs collection for testing.
- Add the new Spectrum ROM, compatible with the new firmware, for updating slot 0 of the Flash 

# Final words:
- Needless to say, there might be many bugs, either on the firmware, the upgrade process or God knows where. We should discuss about a way to deal with discovered bugs and new/improved functions.
- Many functions may be counterintuitive and awkward, and they arise mainly from compromises made either for performance or design limitations. A good example is the need to turn on/off the SD and the IO machines alternativele; this comes from the fact that some pins are shared between those peripherals; other is the need to cache the files in the internal Flash. Some are inherited from previuos versions, but surely many things can be improved 
- Once you get the grasp of it, how Gustavo's ROM works and what expect and returns, the interaction is surprisingly simple
- Enjoy!



