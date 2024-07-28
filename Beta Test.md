# TS-Pico Firmware Beta Test 
Thank you for agreeing to help the Pico team test the new firmware.

## Definitions

**TS-Pico**: The whole enchillada: the assembled printed circuit board and all components.
**Raspberry Pi Pico** or **Pico**: Just the Rasperry Pi Pico component. It may be socketed.
**Flash ROM** or **Flash**: the SST 39SF040 chip on the TS-Pico. It is mounted in a socket.
**P10**: The set of pins that, with a small connector, enables the /WR signal to the Flash ROM and static RAM. It is to the right of the Flash ROM.
**UF2**: A special file that contains the MicroPython interpreter and core TS-Pico functionality code, pre-compiled for better performance.

## The testing board

You have received standard TS-Pico hardware with a pre-programmed Raspberry Pi Pico and the Pico-custom ROM image on flash. 

The P10 jumper (to the right of the flash IC) should be connected on your TS-Pico. On a production TS-Pico, this jumper is open by default, so the /WR signal doesn´t reach either the Flash or SRAM. It must to be enabled for some of the features we'll test.

If it is not, please connect it now.

<img src="/P10_location.jpg" alt="Install this jumper" width="400"> 

## The new firmware

The new firmware updates the following features:
- Improved LOAD caching and streaming to the TS2068.
- LOAD routine validates the block type, preventing errors from loading the incorrect block type.
- Correct small errors in mounting files. Remounting an already mounted TAP file moves the block pointer to the first block.
- Improved file mounting.
- Better handling for loading non-existent files.
- Incorrect commands can show a description of the error condition if verbose is enabled.
- Improved handling for missing or non-working SD card.
- Improved handing for LOAD attempts without a mounted TAP file.

New features include:
- Appending to currently mounted TAP file on SAVE
- "Looping" of TAP files, consistent with behavior in emulators (FUSE, ZEsarUX)
- New commands for better user experience.

## Restoring your TS-Pico

There may be times when you need to "wipe" the firmware and return the TS-Pico to the state it was when you received it.

You will need a [USB to Micro USB](https://www.google.com/search?q=micro+usb) cable and [Thonny](https://thonny.org/) [installed on your computer](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2). 

### First, wipe the Pico and restore the UF2 firmware
1. Remove the TS-Pico from the expansion slot board.
2. [Plug TS-Pico into the Micro USB cable](images/Pico-Top-Plug-v2.png).
3. [Press and hold the BOOTSEL button](images/Pico-bootsel.png), press and release the Pico Reset button (top-most of the 3 pushbuttons on the right), then release the BOOTSEL button.
4. The [Raspberry Pi Pico will appear as a file system device on your computer](images/RPI%20file%20device.png), just as if you'd plugged in a USB thumbdrive.
5. Download [flash-nuke.uf2](firmware/flash_nuke.uf2) to your computer.
6. Drag flash-nuke.uf2 to the Pico device. The Pico will automatically unmount during this process. Mac users: your computer will report this as a problem. It's not.
7. This UF2 will wipe all internal Raspberry Pi Pico memory back to a clean slate. This takes a second or two.
8. The Pico will re-appear as a file system device on your computer.
9. Download the [new uf2 file](firmware/new_firmware_v1.1.uf2) (new_firmware_v1.1.uf2) to your computer.
10. Drag the new uf2 file to your computer. The TS-Pico will automatically unmount during this process.

### Next, restore the TS-Pico MicroPython code and support files

1. Download the "src/src_new_v1.1" folder to your computer.
2. Open Thonny.
4. Ensure you have a [Files browser tab](images/Files%20browser.png) available. If you do not see it, go to View and select Files.
5. Navigate to the *src_new_v1.1* folder on your computer. Once you get there, you should see a TS folder and three files.
6. If the Files browser is one large window, click the Stop button to get the Pico's attention. Your Files browser should have a split, showing the Pico ([like this](images/Files-browser-split.png)).
7. In Thonny, right-click on the TS folder and select ["Upload to /"](images/Upload%20to%20Pico.png). This will upload the folder and its contents to the Pico. **Note:** Don't try to upload this folder and the other files all at once. For some reason, Thonny gets confused and puts the files that should be in the TS folder at the top level.
8. Select the 3 top level files (activity.log, config.ini, and main.py), right-click and select "Upload to /". Your Files browser should list the same files on your computer and on the Pico.
9. **Make sure you have an SD card plugged in to the TS-Pico.** Don't make mistake David makes all the time.
10. Double-click on *main.py* to open it in the editor.
11. Click on the main.py tab if it's not already the focus.
12. Click the RUN icon (green with white "play" icon).
13. In the Shell tab (usually at the bottom of your screen), you should see the following message:

```
MPY: soft reboot
270000000
````

## Testing procedure

Our goals in this beta are to:
1. Ensure the hardware works as advertised
2. Find and squash bugs

If you do not have a GitHub account, please [create one now](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

### Repeatability is key

It's take notes when you are testing the TS-Pico: we will need as much information as possible about issues when you report them, including all the steps you took from power-on or reset. The more information you provide, the easier it may be for us to replicate.


