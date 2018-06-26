#!/usr/bin/env python
import spidev
import time
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=7629
def soil_init():
    adcnum=0
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    print "Threshold",adcout
    return adcout
while 1:
 soil=soil_init()
 temp=((soil*330)/float(1023))
 print temp
 time.sleep(0.5)

