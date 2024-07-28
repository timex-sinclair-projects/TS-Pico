# TS-Pico Firmware Beta Test 
Thank you for agreeing to help the Pico team test the new firmware.

## The testing board

You have received standard TS-Pico hardware with a pre-programmed Raspberry Pi Pico and the Pico-custom ROM image on flash. 

The P10 jumper (to the right of the flash IC) should be connected on your TS-Pico. On a production TS-Pico, this jumper is open by default, so the /WR signal doesn´t reach either the Flash or SRAM. It must to be enabled for some of the features we'll test.

If it is not, please connect it now.

<img src="/P10_location.jpg" alt="Install this jumper" width="800"> 

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

1. Remove the TS-Pico from the expansion slot board.
2. Plug TS-Pico into the Micro USB cable
3. Press and hold the BOOTSEL button, press and release the Pico Reset button (top-most of the 3 pushbuttons on the right), then release the BOOTSEL button.
4. Your TS-Pico will appear as a file system device on your computer, just as if you'd plugged in a USB thumbdrive.
5. Download the nuke-pico.uf2 file to your computer.
6. Drag nuke-pico.uf2 to the TS-Pico device. The TS-Pico will automatically unmount during this process. Mac users: your computer will report this as a problem. It's not.
7. This UF2 will wipe all internal Raspberry Pi Pico memory back to a clean slate. This takes a second or two.
8. Your TS-Pico will re-appear as a file system device on your computer.
9. Download the new uf2 file to your computer.
10. Drag the new uf2 file to your computer.

## Testing procedure

Our goals in this beta are to:
1. Ensure the hardware works as advertised
2. Find and squash bugs

If you do not have a GitHub account, please [create one now](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

### Repeatability is key

It's take notes when you are testing the TS-Pico: we will need as much information as possible about issues when you report them, including all the steps you took from power-on or reset. The more information you provide, the easier it may be for us to replicate.


