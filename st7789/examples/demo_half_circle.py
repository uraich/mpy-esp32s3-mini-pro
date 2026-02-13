from machine import Pin, SPI
from random import random, seed
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff
import sys

try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure that hw_esp32s3_mini_pro.py is uploaded to /lib")
    sys.exit()

try:
    from st7789py import *
    import st7789_config
except:
    print("Please make sure that st7789py.py and st7789_config.py are uploaded to /lib before running this program")
    sys.exit()    

def half_circle(x0, y0, r, color):
    """Draw a circle.
        
        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
    """
    f = 1 - r
    dx = 1
    dy = -r - r
    x = 0
    y = r
    #display.pixel(x0, y0 + r, color)
    display.pixel(x0, y0 - r, color)
    display.pixel(x0 + r, y0, color)
    display.pixel(x0 - r, y0, color)
    while x < y:
        if f >= 0:
            y -= 1
            dy += 2
            f += dy
        x += 1
        dx += 2
        f += dx
        #display.pixel(x0 + x, y0 + y, color)
        #display.pixel(x0 - x, y0 + y, color)
        display.pixel(x0 + x, y0 - y, color)
        display.pixel(x0 - x, y0 - y, color)
        #display.pixel(x0 + y, y0 + x, color)
        #display.pixel(x0 - y, y0 + x, color)
        display.pixel(x0 + y, y0 - x, color)
        display.pixel(x0 - y, y0 - x, color)

display=st7789_config.config()
display.fill(0)
half_circle(64,64,63,display.GREEN)
display.hline(0,64,127,display.GREEN)

