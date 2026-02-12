# switchesAndLed.py: This program is an improved version of https://github.com/CsErik2001/Lolin-S3-Mini-Pro by
# Csontos Erik 
# It has been re-written by U. Raich, 12. Feb. 2026
# The program reads the 3 user switches and changes the color of the LED depending on the switches pressed
# left switch:   red
# middle switch: green
# right switch:  blue

from time import sleep_ms
from neopixel import NeoPixel
from machine import Pin,Signal
import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()

# Ensure RGB LED power is enabled
led_pwr = Pin(NEOPIXEL_PWR, Pin.OUT)           # power for the LED
led_pwr.on()                                   # turn LED power on

rgb_led = NeoPixel(Pin(NEOPIXEL),NO_OF_NEOPIXELS)

# here we use the Signal class, allowing to select if the signal is active low (invert = True) or active high
switches = [Signal(Pin(USER_SWITCH_0, Pin.IN, Pin.PULL_UP),invert=True),  
            Signal(Pin(USER_SWITCH_47, Pin.IN, Pin.PULL_UP),invert=True),
            Signal(Pin(USER_SWITCH_48, Pin.IN, Pin.PULL_UP),invert=True)]

current_state = [-1,-1,-1]               # undefined

def write_led(color):                    # parameter is a tuple of (r,g,b) values
    rgb_led[0] = color
    rgb_led.write()
    
while True:
    # read the current state of the switches
    button_state = [switches[0].value(),switches[1].value(),switches[2].value()]
    if button_state == current_state:
        sleep_ms(100)  # Debounce delay
        continue
    else:
        current_state = button_state
    # Check for all possible combinations of button presses
    if button_state[0] and button_state[1] and button_state[2]: # White (Red + Green + Blue)
        write_led((INTENSITY, INTENSITY, INTENSITY))  
        print("Button 0 (Red), Button 47 (Green), and Button 48 (Blue) pressed: White")
        
    elif button_state[0] and button_state[1]:  # Red Green buttons pressed together
        write_led((INTENSITY, INTENSITY, 0))   #  (Red + Green)
        print("Button 0 (Red) and Button 47 (Green) pressed: Yellow")

    elif button_state[1] and button_state[2]:  # Blue and Green buttons pressed together
        write_led((INTENSITY, 0, INTENSITY))   # Cyan (Green + Blue)
        print("Button 47 (Green) and Button 48 (Blue) pressed: Cyan")

    elif button_state[0] and button_state[2]:  # Red and Blue buttons pressed together
        write_led((0, INTENSITY, INTENSITY))   # Magenta (Red + Blue)
        print("Button 47 (Red) and Button 48 (Green) pressed: Magenta")
        
    elif button_state[0]  :                    # Button 0 pressed (Blue)
        write_led((0, INTENSITY, 0))           # Red
        print("Button 0 (Red) pressed: Red")

    elif button_state[1]:                      # Button 47 pressed (Green)
        write_led((INTENSITY, 0, 0))           # Green
        print("Button 47 (Green) pressed: Green")

    elif button_state[2]:                      # Button 48 pressed (Blue)
        write_led((0, 0, INTENSITY))           # Blue
        print("Button 48 (Blue) pressed: Blue")
    else:
        write_led((0, 0, 0))  
        print("No button pressed: LED off")
        

