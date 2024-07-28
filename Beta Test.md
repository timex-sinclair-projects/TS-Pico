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

## Testing procedure

Our goals in this beta are to:
1 Ensure the hardware works as advertised
2 Find and squash bugs

If you do not have a GitHub account, please [create one now](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
