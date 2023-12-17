import time, utime

from gc import mem_free, collect
from machine import freq, Pin

#from TS.TPI_backend_RC5 import TS2068_IO
from tspico import TS2068_IO

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

led = Pin(25, Pin.OUT)

led.value(1)
utime.sleep(2)

for f in range(6):
    led.toggle()
    utime.sleep(.1)

led.value(0)

freq(270_000_000)
print(freq())

while True:
    
    collect()
    # print("Free mem at start: " + str(mem_free()))
    
    TS2068_IO()
