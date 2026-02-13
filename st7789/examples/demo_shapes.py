"""ST7789 demo (shapes)."""

from machine import Pin, SPI
from time import sleep
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
    display.fill(display.BLACK)
    print('display started')

    display.fill(color565(64, 0, 255))
    sleep(1)

    display.fill(display.BLACK)

    display.hline(10, 127, 63, color565(255, 0, 255))
    sleep(1)

    display.vline(10, 0, 127, color565(0, 255, 255))
    sleep(1)

    display.fill_rect(23, 50, 30, 75, color565(255, 255, 255))
    sleep(1)

    display.hline(0, 0, 127, color565(255, 0, 0))
    sleep(1)

    display.line(127, 0, 64, 127, color565(255, 255, 0))
    sleep(2)

    display.fill(display.BLACK)

    '''
    coords = [[0, 63], [78, 80], [122, 92], [50, 50], [78, 15], [0, 63]]
    display.draw_lines(coords, color565(0, 255, 255))
    sleep(1)

    display.clear()
    display.draw_filledPolygon(7, 63, 63, 50, color565(0, 255, 0))
    sleep(1)
    '''
    display.fill_rect(0, 0, 15, 127, color565(255, 0, 0))
    sleep(1)

    display.fill(display.BLACK)

    display.fill_rect(0, 0, 63, 63, color565(128, 128, 255))
    sleep(1)

    display.rect(0, 64, 63, 63, color565(255, 0, 255))
    sleep(1)

    display.fill_rect(64, 0, 63, 63, color565(128, 0, 255))
    sleep(1)

    display.regular_polygon(3, 96, 96, 30, color565(0, 64, 255),
                            rotate=15)

    sleep(3)

    display.fill(display.BLACK)

    display.fill_circle(32, 32, 30, color565(0, 255, 0))
    sleep(1)

    display.circle(32, 96, 30, color565(0, 0, 255))
    sleep(1)

    display.fill_ellipse(96, 32, 30, 16, color565(255, 0, 0))
    sleep(1)

    display.ellipse(96, 96, 16, 30, color565(255, 255, 0))

    sleep(5)
    display.fill(display.BLACK)


test()
