# input pins for esp32s3 mini pro

from machine import Pin

class Buttons():
    def __init__(self):
        self.name = "esp32s3 mini pro"
        self.left = Pin(0, Pin.IN, Pin.PULL_UP)
        self.right = Pin(48, Pin.IN, Pin.PULL_UP)
