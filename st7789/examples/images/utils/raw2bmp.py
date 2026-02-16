#!/bin/python3
# Converts raw images to bitmap format
# This allows to display the converted images with standard image display tools
# like eog
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

# Create the file header for the bmp file
BI_BITFIELDS = 3
# This is how you define rgb565 pixel format 
colorMaskRed   = 0xf800
colorMaskGreen = 0x07e0
colorMaskBlue  = 0x001f
colorMask = struct.pack("III",colorMaskRed,colorMaskGreen,colorMaskBlue)
# print(len(colorMask))
# print(colorMask)

# Now the info header
BI_RGB = 0
infoHeader = bytearray(40)
infoHdrSize = len(infoHeader)
imageWidth = width
imageHeight = height
noOfPlanes = 1
noOfBitsPerPixel = 16
compression = BI_BITFIELDS              # the bit fields define rgb565 pixel format
imageSize = 0                           # this works for uncompressed images
imageSize = imageWidth * imageHeight * 2
hor_resolution = 0                      # no preference
ver_resolution = 0                      # no preference
noOfColors = 0                          # only used with color maps
importantColors = 0
infoHdr = struct.pack("3i2h6i",infoHdrSize,imageWidth,imageHeight,noOfPlanes,
                      noOfBitsPerPixel,compression,imageSize,
                      hor_resolution,ver_resolution,
                      noOfColors,importantColors)

# and the file header
fileHdrSize = 14
magic = 'BM'.encode('ascii')
fileSize = fileHdrSize + len(infoHdr) + len(colorMask) + width*height*2
reserved = 0
offset = fileHdrSize + len(infoHdr) + len(colorMask)
hdr = magic + struct.pack('iHHi',fileSize,reserved,reserved,offset)
print("File header: ")
for i in range(len(hdr)-1):
    print("0x{:02x}, ".format(hdr[i]),end="")
print("0x{:02x}, ".format(hdr[i]))

# The pixel values in the bitmap file are little endian. We must therefore
# swap each pixel word

pixels_swapped = bytearray(width*height*2)
for i in range(width*height):
    pixels_swapped[2*i] = pixels_raw_ba[2*i+1]
    pixels_swapped[2*i+1] = pixels_raw_ba[2*i]

# In the bmp file the rows are upside down: first y position is at the bottom
upside_down = bytearray()
for col  in range(height-1,-1,-1):
    # print(col*width*2,":",(col+1)*width*2)
    row = pixels_swapped[col*width*2: (col+1)*width*2]
    if len(row) % 4:
        row = row + bytes([0,0]) # pad to 4 byte boundary
    upside_down = upside_down + row

# We open binary bmp file where we deduct the filename from the original
# file name of the raw pixel file
# rsplit('.',1) splits starting from the right and splits only on the first '.'

bmp_filename = filename.rsplit('.',1)[0] + ".bmp"
print("Writing to ",bmp_filename)
# The sequence is:
# file header
# info header
# color mask
# pixel data

bmp_file = open(bmp_filename,"wb")
# write the header
bmp_file.write(hdr)
bmp_file.write(infoHdr)
bmp_file.write(colorMask)
bmp_file.write(upside_down)
bmp_file.close()
