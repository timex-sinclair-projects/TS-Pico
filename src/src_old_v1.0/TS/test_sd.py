import time, utime, gc, os
from machine import Pin, freq, SPI

from TS.sdcard import *

def REMOVE_DIR(d):                                                        # Recursively remove a directory and all its contents
    
    try:
        if os.stat(d)[0] & 0x4000:  # Dir
            for f in os.ilistdir(d):
                if f[0] not in ('.', '..'):
                    REMOVE_DIR("/".join((d, f[0])))  # File or Dir
            os.rmdir(d)
        else:  # File
            os.remove(d)
        
    except:
        print("WARNING: could not remove directory " + d)
        
    return


U3_CS       = Pin(28, Pin.OUT, Pin.PULL_UP)
D0          = Pin(2,  Pin.IN)
D1          = Pin(3,  Pin.IN)
D2          = Pin(4,  Pin.IN)

spi = SPI(0, sck=D0, mosi=D1, miso=D2)
sd = SDCard(spi, U3_CS)
    
os.mount(sd, "/sd")
# REMOVE_DIR("/sd/UPD")        

os.umount("/sd")
