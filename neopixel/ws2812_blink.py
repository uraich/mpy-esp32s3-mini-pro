# ws2812_blink.py: blink the user LED on the esp32s3-mini-pro board
# The wemos esp32s3-mini-pro board uses a ws2812 neopixel
# Copyright (c) U. Raich 9. Feb. 2026
# This program is part of the course on tinyML at the
# University of Cape Coast, Ghana
# It is released under the MIT license

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms
import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()

ON         = 1
OFF        = 0

led_pwr = Pin(NEOPIXEL_PWR,Pin.OUT)

# power the neopixel
led_pwr.on()

led = NeoPixel(Pin(NEOPIXEL),NO_OF_NEOPIXELS)

def switchLED(onOff):
    if onOff:
        led[0] = (0,0,INTENSITY)
    else:
        led[0]  = (0,0,0)
    led.write()

def led_on():
    switchLED(ON)

def led_off():
    switchLED(OFF)

try:
    while True:
        led_on()
        sleep_ms(500)
        led_off()
        sleep_ms(500)
except KeyboardInterrupt:
    led_off()
    led_pwr.off()
