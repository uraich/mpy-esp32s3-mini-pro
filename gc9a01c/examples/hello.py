"""
hello.py
========

.. figure:: /_static/hello.png
  :align: center

Writes "Hello!" in random colors at random locations on the display.
"""

import random

import vga1_bold_16x32 as font
import gc9a01
import tft_config
from time import sleep_ms
import sys

tft = tft_config.config()

col_max = tft.width() - font.WIDTH * 6
row_max = tft.height() - font.HEIGHT

print("col_max: ",col_max)
print("row_max: ",row_max)

def main():

    tft.init()
    tft.offset(2,1)  #offset for 0.85  GC9107
    tft.fill(0)
    '''
    sleep_ms(1000)
    
    for rotation in range(8):
        tft.rotation(rotation)
        tft.text(
            font,
            "Hello!",
            random.randint(0, col_max),
            random.randint(0, row_max),
            gc9a01.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ),
            gc9a01.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8),
            ))
        sleep_ms(5000)
        tft.fill(0)
    '''
    try:
        while True:
            for rotation in range(4,8):
                tft.rotation(rotation)
                # tft.fill(0)
                # col_max = tft.width() - font.WIDTH * 6
                # row_max = tft.height() - font.HEIGHT
                
                for _ in range(64):
                    tft.text(
                        font,
                        "Hello!",
                        random.randint(0, col_max),
                        random.randint(0, row_max),
                        gc9a01.color565(
                            random.getrandbits(8),
                            random.getrandbits(8),
                            random.getrandbits(8),
                        ),
                        gc9a01.color565(
                            random.getrandbits(8),
                            random.getrandbits(8),
                            random.getrandbits(8),
                        ),
                    )
                    sleep_ms(100)
    except KeyboardInterrupt:
        tft.fill(0)
        sys.exit(0)
main()
