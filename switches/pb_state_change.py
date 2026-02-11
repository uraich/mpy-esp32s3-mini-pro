# pb_state_change.py: Reads and prints the state of the pushbuttons every 100 ms
# Signals only state changes
# This is part of the TinyML course at the 
# University of Cape Coast, Ghana
# Copyright (c) U.Raich 10. Feb. 2026
# The program is released under the MIT license

import sys
from machine import Pin
from time import sleep_ms

import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()
    
switches = [Pin(USER_SWITCH_0, Pin.IN, Pin.PULL_UP),  
            Pin(USER_SWITCH_47, Pin.IN, Pin.PULL_UP),
            Pin(USER_SWITCH_48, Pin.IN, Pin.PULL_UP)]

current_state = [switches[0].value(),switches[1].value(),switches[2].value()]
current_state_string = [""]*3
for sw in range(3):
    if current_state[sw] == 1:
        current_state_string[sw] = "open"
    else:
        current_state_string[sw] = "closed"
print("Current switch state:")
print("left: {:s}, middle: {:s}, right: {:s}".format(
    current_state_string[0],
    current_state_string[1],
    current_state_string[2]))

def printState(switchIndex,state):
    if switchIndex == 0:
        if state:
            print("Left switch is now open")
        else:
            print("Left switch is now closed")
    elif switchIndex == 1:
        if state:
            print("Middle switch is now open")
        else:
            print("Middle switch is now closed")
    else:
        if state:
            print("Right switch is now open")
        else:
            print("Right switch is now closed")
try:
    while True:
        for sw in range(3):
            tmp =  switches[sw].value()
            # check if switch state has changed. If yes, print a message
            # and update the state
            if current_state[sw] != tmp:
                current_state[sw] = tmp
                printState(sw,tmp)
        sleep_ms(100) # do this every 100 ms
except KeyboardInterrupt:
    sys.exit(0)
