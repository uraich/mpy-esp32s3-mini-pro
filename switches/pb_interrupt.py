# pb_interrupts.py: reads the user switches on the esp32s3 mini pro
# The button generates and interrupt when pressed
# Copyright (c) U. Raich, Feb, 2026
# This program is part of a course on tinyML for the
# University of Cape Coast, Ghana
# It is released under the MIT license

from machine import Timer
import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()

from time import sleep_ms

switches = [Pin(USER_SWITCH_0, Pin.IN, Pin.PULL_UP),  
            Pin(USER_SWITCH_47, Pin.IN, Pin.PULL_UP),
            Pin(USER_SWITCH_48, Pin.IN, Pin.PULL_UP)]

timer0 = Timer(0)
debounce = False

def debounceDone(src):
    global debounce
    debounce = False
    
# define the Interrupt service routine
# In order to software-debounce the switch, we start a one-shot timer
# and neglect any interrupt triggers for 20 ms
# The src parameter tells us, which switch has triggered

def callback(src):
    global debounce,timer0,switches
    if debounce:
        return
    else:
        debounce = True
        timer0 = Timer(0)
        timer0.init(period=20, mode=Timer.ONE_SHOT, callback=debounceDone)
        if src == switches[0]:
            print("switch 0 was pressed")
        elif src == switches[1]:
            print("switch 47 was pressed")
        else:
            print("switch 48 was pressed")

        # print(src)

# connect the IRG to its handler
# Since the signal is active low (switch reads 1 when not pressed)
# we look at the falling edge of the signal 
for switch in switches:
    switch.irq(trigger=Pin.IRQ_FALLING, handler = callback)

print("Switches test with interrupts")
print("Please press one of the buttons")
try:
    while True:
        pass
except KeyboardInterrupt:
    sys.exit(0)
