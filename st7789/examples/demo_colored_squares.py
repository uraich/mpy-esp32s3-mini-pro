"""ST7789 demo (colored squares)."""
from time import sleep
from machine import Pin, SPI
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

def test():    
    """Test code."""

    display=st7789_config.config()
    # clear the display
    display.fill(0)
    
    colors= [display.RED,display.GREEN,display.BLUE,display.YELLOW,
             display.MAGENTA,display.AQUA,display.MAROON,display.DARKGREEN,
             display.NAVY,display.TEAL,display.PURPLE,display.OLIVE,
             display.ORANGE,display.DEEP_PINK,display.CHARTREUSE,
             display.SPRING_GREEN,display.INDIGO,display.DODGER_BLUE,
             display.CYAN,display.PINK,display.LIGHT_YELLOW,
             display.LIGHT_CORAL,display.LIGHT_GREEN,
             display.LIGHT_SLATE_BLUE,display.WHITE]
    # colors.sort()
    c = 0
    for x in range(1, 126, 25):
        for y in range(1, 126, 25):
            display.fill_rect(x, y, 25, 25, colors[c])
            c += 1
    sleep(9)
    display.fill(0)



test()
