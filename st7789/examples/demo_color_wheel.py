"""ST7789 demo (color wheel)."""
from time import sleep
from machine import Pin, SPI
from math import cos, pi, sin
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
   
HALF_WIDTH = const(64)
HALF_HEIGHT = const(64)
CENTER_X = const(63)
CENTER_Y = const(63)
ANGLE_STEP_SIZE = 0.05  # Decrease step size for higher resolution
PI2 = pi * 2


def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB (based on colorsys.py).

        Args:
            h (float): Hue 0 to 1.
            s (float): Saturation 0 to 1.
            v (float): Value 0 to 1 (Brightness).
    """
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    v = int(v * 255)
    t = int(t * 255)
    p = int(p * 255)
    q = int(q * 255)

    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


def test():
    """Test code."""
    
    display=st7789_config.config()
    display.fill(display.BLACK)
    x, y = 0, 0
    angle = 0.0
    #  Loop all angles from 0 to 2 * PI radians
    while angle < PI2:
        # Calculate x, y from a vector with known length and angle
        x = int(CENTER_X * sin(angle) + HALF_WIDTH)
        y = int(CENTER_Y * cos(angle) + HALF_HEIGHT)
        color = color565(*hsv_to_rgb(angle / PI2, 1, 1))
        c0 = color & 0xff
        c1 = color >> 8
        # print("color: {:02x} {:02x}".format(c1,c0))
        display.line(x, y, CENTER_X, CENTER_Y, color)
        angle += ANGLE_STEP_SIZE

    sleep(5)
    
    display.fill(display.BLACK)
    for r in range(CENTER_X, 0, -1):
        color = color565(*hsv_to_rgb(r / HALF_WIDTH, 1, 1))
        display.fill_circle(CENTER_X, CENTER_Y, r, color)

    sleep(9)
    display.fill(display.BLACK)

test()
