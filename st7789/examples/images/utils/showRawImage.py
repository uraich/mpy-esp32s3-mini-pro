#!/bin/python3
# Display the raw images
# Converts the rgb565 images to 24 bit rgb values and prints the image to the
# screen using the PIL library
# Copyright (c) U. Raich, 16.2.2026
# This program is part of the IoT course at the University of Cape Coast, Ghana
# It is released under the MIT license

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import re
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: {:s} filename.raw".format(sys.argv[0]))
    sys.exit(-1)
    
filename = sys.argv[1]
print("filename: ",filename)

# search for the first digit in the filename
m = re.search(r"\d", filename)
if not m:
    print("Invalid file name. Filename must contain image size as width x height")
    sys.exit(-1)
    
tmp = filename[m.start():].split('.')[0]
print("Image size is {:s} pixels".format(tmp))

size = tmp.split('x')
width = int(size[0])
height = int(size[1])
print("width: {:d}, height: {:d}".format(width,height))

# Now that we the width and height ofthe pixel image, let's read the file
f = open(filename,"rb")
pixels_raw_ba = bytearray(f.read())
f.close()

# The pixel data come as a byte array and the 16 bit unsigned pixel values must be extracted
pixels_raw = []
for i in range(width*height):
    ba_pixel = pixels_raw_ba[(i*2):(i*2+2)]
    pixels_raw.append(struct.unpack('>H',ba_pixel)[0])

# Let's print a few pixel values. These can be compared to the file with ghex
print("Type of pixel values: ",type(pixels_raw[0]))
print("A few pixel values:")
for p in range(0,16):
    print("0x{:04x}, ".format(pixels_raw[p]),end="")
print("")

# Now we create a numpy array and reshape it into a width x height matrix
pixels_rgb565 = np.array(pixels_raw, dtype=np.uint16)
pixels_rgb565 = pixels_rgb565.reshape((width,height))

# Now 8 bit r,g,b values are extracted from the rgb565 format
pixels = np.empty((width,height,3), dtype=np.uint8)
for col in range(height):
    for row in range(width):
        tmp = pixels_rgb565[row][col]
        pixels[row][col][0] = (tmp >> 8) & 0xf8  # red component
        pixels[row][col][1] = (tmp >> 3) & 0xfc  # green
        pixels[row][col][2] =  tmp << 3
        
# ... and finally we can plot the image 
image = Image.frombytes('RGB',(width,height),pixels)
image.show()
