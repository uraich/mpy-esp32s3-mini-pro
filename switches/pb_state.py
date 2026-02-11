# pb_state.py: reads the user switches on the esp32s3 mini pro
# Copyright (c) U. Raich, Feb, 2026
# This program is part of a course on tinyML for the
# University of Cape Coast, Ghana
# It is released under the MIT license

import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()

from time import sleep_ms
from machine import Pin,Signal
switches = [Pin(USER_SWITCH_0, Pin.IN, Pin.PULL_UP),  
            Pin(USER_SWITCH_47, Pin.IN, Pin.PULL_UP),
            Pin(USER_SWITCH_48, Pin.IN, Pin.PULL_UP)]

switch_status = [""]*3
print("Status of the 3 user switches:")
while True:
    for sw in range(3):
        if switches[sw].value():
            switch_status[sw] = "open"
        else:
            switch_status[sw] = "closed"
    print("left: {:s}, middle: {:s}, right: {:s}".format(
        switch_status[0],switch_status[1],switch_status[2]))
    sleep_ms(100)
    



