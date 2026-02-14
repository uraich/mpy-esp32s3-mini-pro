"""
rotations.py
============

.. figure:: /_static/rotations.png
  :align: center

  Shows the effect of each of the 8 rotation values on the display.
"""

import utime
import gc9a01
import tft_config
import vga1_8x16 as font


def main():
    tft = tft_config.config()

    tft.init()
    tft.offset(2,1)
    tft.fill(gc9a01.BLACK)
    utime.sleep(1)

    try:
        while True:
            for rot in range(8):
                # print("Rotation: ",rot)
                tft.fill(gc9a01.BLACK)
                tft.rotation(rot)
                s = f"Rotation {rot}"
                tft.text(font, s, 20, 64, gc9a01.WHITE)
                utime.sleep(2)
    except KeyboardInterrupt:
        tft.fill(gc9a01.BLACK)
main()

