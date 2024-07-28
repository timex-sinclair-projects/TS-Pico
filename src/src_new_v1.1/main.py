import time, utime, sys

from gc import mem_free, collect
from machine import freq, Pin

from TS.tspico import TS2068_IO
# from tspico import TS2068_IO

U6_EN = Pin(12, Pin.OUT, Pin.PULL_UP)
WAIT = Pin(14, Pin.OUT, Pin.PULL_DOWN)
U10_ENA = Pin(19, Pin.OUT, Pin.PULL_UP)
U13_ENA = Pin(20, Pin.OUT, Pin.PULL_UP)
BE = Pin(21, Pin.OUT, Pin.PULL_UP)
ROSCS = Pin(26, Pin.IN, Pin.PULL_DOWN)
U10_WE = Pin(27, Pin.OUT, Pin.PULL_UP)
 
U6_EN.value(1)
WAIT.value(1)
U10_ENA.value(1)
U13_ENA.value(1)
BE.value(1)
U10_WE.value(1)

freq(270_000_000)
print(freq())

log_msg = ""

utime.sleep(.5)

while True:
    
    collect()
    TS2068_IO()
        
 