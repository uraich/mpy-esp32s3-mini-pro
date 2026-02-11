# hw_esp32_s3_fh4r2.py: defines all the hardware connections of the
# esp32s3-mini-pro CPU
# Copyright (c) U. Raich, Feb. 2026
# This file is part of the course on TinyML at the
# University of Cape Coast, Ghana
# It is released under the MIT license

from micropython import const

# neopixel
NEOPIXEL          = const(8)
NEOPIXEL_PWR      = const(7)
NO_OF_NEOPIXELS   = const(1)
INTENSITY         = const(0x1f)
GRB               = True

# infrared LED
IR                = const(9)

# user switches
USER_SWITCH_0     = const(0)
USER_SWITCH_47    = const(47)
USER_SWITCH_48    = const(48)

# I2C
SCL               = const(11)
SDA               = const(12)

# SPI
SPI_MOSI          = const(38)
SPI_MISO          = const(39)
SPI_CLK           = const(40)

# TFT
TFT_BL            = const(33)
TFT_DC            = const(36)
TFT_CS            = const(35)
TFT_RST           = const(34)
                
# microphone
MIC_WS            = const(26)
MIC_SCK           = const(22)
MIC_SD            = const(21)

MATRIX            = const(16)
NO_OF_MATRIX_LEDS = const(64)
