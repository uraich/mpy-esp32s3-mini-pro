"""ST7735 demo (images)."""
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
    display.fill(display.BLACK)
    
    display.image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.image('images/MicroPython128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.image('images/Tabby128x128.raw', 0, 0, 128, 128)
    sleep(5)

    display.image('images/Tortie128x128.raw', 0, 0, 128, 128)
    sleep(10)

    display.fill(display.BLACK)


test()
