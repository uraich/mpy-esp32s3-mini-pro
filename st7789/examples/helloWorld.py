# helloWorld.py: prints "Hello World!", "Good bye World!" and another
# "Hello World!" in different fonts and different colors
# This is a demo program for the TFT display on the esp32s3 mini pro
# Copyright (c) U. Raich, 11.Feb. 2026
# This program is part of the IoT course at the University of Cape Coast, Ghana
# It is released under the MIT license

from time import sleep
from st7789py import ST7789, BGR, color565
from machine import Pin, SPI
import vga1_8x16 as font_8x16
import vga1_8x8 as font_8x8
import vga2_16x16 as font_16x16

import sys

from time import sleep

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
    
print("Testing the st7789 TFT display on the esp32s3 mini pro")
print("Program written for the course on IoT at the")
print("University of Cape Coast")
print("Copyright: U.Raich")

print("Released under the MIT License")
hSize       = const(128)  # Hauteur ecran en pixels | display heigh in pixels
wSize       = const(128)  # Largeur ecran en pixels | display width in pixels

display = st7789_config.config()

def clear():
    display.fill(0)

def test():

    clear()
    display.text(font_8x16,'Hello World!', 0, 0, color565(255, 255, 0), display.BLACK)
    display.text(font_8x8,'Good bye World!',0,20, color565(255, 0, 255), display.BLACK)
    display.text(font_16x16,'Hello', 0,40, color565(0, 255, 0), display.BLACK)
    display.text(font_16x16,'World!', 0,60, color565(0, 255, 0), display.BLACK)
    sleep(9)



test()
