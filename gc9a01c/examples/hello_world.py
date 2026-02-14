import gc9a01
import tft_config
from time import sleep
import vga1_8x16 as font_8x16
import vga1_8x8 as font_8x8
import vga2_16x16 as font_16x16

tft = tft_config.config()

tft.init()
tft.offset(2,1)  #offset for 0.85  GC9107 
# clear the display
tft.fill(gc9a01.BLACK)

print("Testing the gca01 TFT display on the esp32s3 mini pro")
print("Program written for the course on IoT at the")
print("University of Cape Coast")
print("Copyright: U.Raich")

print("Released under the MIT License")

display = tft_config.config()
tft.init()

def clear():
    tft.fill(gc9a01.BLACK)

def test():

    clear()
    display.text(font_8x16,'Hello World!', 0, 0, gc9a01.color565(255, 255, 0), gc9a01.BLACK)
    display.text(font_8x8,'Good bye World!',0,20, gc9a01.color565(255, 0, 255), gc9a01.BLACK)
    display.text(font_16x16,'Hello', 0,40, gc9a01.color565(0, 255, 0), gc9a01.BLACK)
    display.text(font_16x16,'World!', 0,60, gc9a01.color565(0, 255, 0), gc9a01.BLACK)
    sleep(9)
    clear()


test()
