# TS-Pico Firmware Beta Test 
Thank you for agreeing to help the Pico team test the new firmware.

## The testing board

You have received standard TS-Pico hardware with a pre-programmed Raspberry Pi Pico and the Pico-custom ROM image on flash. 

The P10 jumper (to the right of the flash IC) should be connected on your TS-Pico. If it is not, please connect it now.

INSTALL the jumper on P10 (next to the Flash IC) on your TS-Pico board, or the write to the Flash/SRAM won´t work!

<img src="/P10_location.jpg" alt="Install this jumper" width="800"> 

On a production TS-Pico, this jumper is open by default, so the /WR signal doesn´t reach either the Flash or SRAM. It must to be enabled for some of the features we'll test.
