# graphicstest.py: Tests all sorts of graphics primitives
# Copyright (c)  U. Raich, 11. Feb. 2026
# This program is part of the IoT course at the University of Cape Coast, Ghana
# It is released under the MIT license

from time import sleep
from st7789py import ST7789, BGR
from machine import Pin, SPI
import vga1_8x16 as font_8x16
import time
import math

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
    print("Please make sure that st7789py.py and st7789_config.py are  uploaded to /lib before running this program")
    sys.exit()    
    
print("Testing the st7789 TFT display on the esp32s3 mini pro")
print("Program written for the course on IoT at the")
print("University of Cape Coast")
print("Copyright: U.Raich")
print("Released under the MIT License")

hSize       = const(128)  # Hauteur ecran en pixels | display heigh in pixels
wSize       = const(128)  # Largeur ecran en pixels | display width in pixels

display = ST7789(
        SPI(2, baudrate=40000000, sck=Pin(SPI_CLK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO)),
        wSize,
        hSize,
        reset=Pin(TFT_RST, Pin.OUT),
        cs=Pin(TFT_CS, Pin.OUT),
        dc=Pin(TFT_DC, Pin.OUT),
        backlight=Pin(TFT_BL, Pin.OUT),
        rotation=0,
        color_order= BGR,
    )

def clear():
    display.fill(0)

def testlines(color):
    print("Test lines")
    clear()
    
    for x in range(0, wSize, 6):
        display.line(0, 0, x, hSize - 1, color)

    for y in range(0, hSize, 6):
        display.line(0, 0, wSize - 1, y, color)        
    clear()
        
    for x in range(0, hSize, 6):
        display.line(wSize - 1, 0, x, hSize - 1, color)

    for y in range(0, hSize, 6):
        display.line(wSize - 1, 0, 0, y, color)        
    clear()
    
    for x in range(0, wSize, 6):
        display.line(0, hSize - 1, x, 0, color)
        
    for y in range(0, wSize, 6):
        display.line(0, hSize - 1, wSize - 1,y, color)
    clear()

    for x in range(0, wSize, 6):
        display.line(wSize - 1, hSize - 1, x, 0, color)

    for y in range(0, hSize, 6):
        display.line(wSize - 1, hSize - 1, 0, y, color)
        
def testfastlines(color1, color2):
    print("Test horizontal and vertical fast lines") 
    clear()
    for y in range(0, hSize, 5):
        display.hline(0, y, wSize, color1)
    
    for x in range(0, wSize, 5):
        display.vline(x,0, hSize, color2)

       
def testdrawrects(color):
    print("Test rectangles")         
    clear()
    
    for x in range(0,wSize,6):
        display.rect(wSize//2 - x//2, hSize//2 - x//2, x, x, color)
        
def testfillrects(color1, color2):
    print("Test filled rectangles")     
    clear()
    for x in range(wSize,0,-6):
        display.fill_rect(wSize//2 - x//2, hSize//2 - x//2, x, x, color1)
        display.rect(wSize//2 - x//2, hSize//2 - x//2, x, x, color2)
    

def testfillcircles(radius, color):
    print("Test filled circles")
    clear()
    for x in range(radius, wSize, radius * 2):
        for y in range(radius, hSize, radius * 2):
            display.fill_circle(x, y , radius, color)
        
def testdrawcircles(radius, color):
    print("Test circles")
    for x in range(0, wSize + radius, radius * 2):
        for y in range(0, hSize + radius, radius * 2):
            display.circle(x, y, radius, color)

            
def testtriangles():
    print("Test triangles")
    clear()
    color = 0xF800
    w = wSize // 2
    x = hSize - 1
    y = 0
    z = wSize
    for t in range(0, 15):
        display.line(w, y, y, x, color)
        display.line(y, x, z, x, color)
        display.line(z, x, w, y, color)
        x -= 4
        y += 4
        z -= 4
        color += 100
        
def testroundrects():
    print("Test differently colored rectangles")
    clear()
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = wSize - 2
        h = hSize - 2
        for i in range(17):
            display.rect(x, y, w, h, color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

def tftprinttest():
    clear()
    print("Test text printing")
    v = 0
    display.text(font_8x16, "Hello World!", 0, v, display.RED)
    v += font_8x16.HEIGHT
    display.text(font_8x16, str(math.pi), 0, v, display.GREEN)
    v += font_8x16.HEIGHT
    display.text(font_8x16, " Want pi?", 0, v, display.GREEN)
    v += font_8x16.HEIGHT 
    display.text(font_8x16, hex(8675309), 0,v, display.GREEN)
    v += font_8x16.HEIGHT
    display.text(font_8x16, " Print HEX!", 0, v, display.GREEN)
    v += font_8x16.HEIGHT
    display.text(font_8x16, "Sketch has been", 0, v, display.WHITE)
    v += font_8x16.HEIGHT
    display.text(font_8x16, "running for: ", 0, v, display.WHITE)
    v += font_8x16.HEIGHT
    display.text(font_8x16, str(time.ticks_ms() / 1000), 0, v, display.PURPLE)
    v += font_8x16.HEIGHT
    display.text(font_8x16, " seconds.", 0, v, display.WHITE)

def tfttesttextwrap():
    clear()
    print("Test text wrapping")
    display.text(font_8x16,"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", 0, 0, display.GREEN)
    time.sleep(1)    
    clear()
    '''
    tft.text(0,127, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", Display.WHITE,landscape=True)
    tft.show()
    time.sleep(1)
    tft.fill(0)
    tft.show()
    '''

def test_main():
    '''
    tfttesttextwrap()
    time.sleep(2)
    ''' 
    tftprinttest()
    time.sleep(10)

    testlines(display.YELLOW)
    time.sleep(2)

    testfastlines(display.RED, display.BLUE)
    time.sleep(2)
    
    testdrawrects(display.GREEN)
    time.sleep(2)

    testfillrects(display.YELLOW, display.PURPLE)
    time.sleep(2)
    
    clear()
    testfillcircles(10, display.BLUE)
    testdrawcircles(10, display.WHITE)
    time.sleep(2)
    
    testroundrects()
    time.sleep(2)

    testtriangles()
    time.sleep(2)
    
test_main()

