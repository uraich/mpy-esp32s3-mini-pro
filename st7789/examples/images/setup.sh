#!/bin/bash
# This shell scripts sets up the picoweb server to run the Hello World
# WEB server. It uses picoweb to provide the Hello World WEB page.
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under GPL

echo "Uploads the image files to /images"
dirs="$(ampy ls)"
echo $dirs

#check if /images already exists

if [[ $dirs == *"/images"* ]]
then
    echo "/images directory already exists"
    echo "The following modules have been uploaded to /images:"
    modules="$(ampy ls /images)"
    for i in $modules ; do
	echo ${i#"/images/"}
	done    
else
    echo "Creating /images directory"
    ampy mkdir /images
fi

echo ""
echo "Uploading the images will take quite some time! Please be patient!"
echo "Uploading blinka45x48.raw"
ampy put blinka45x48.raw /images/blinka45x48.raw
echo "Uploading Mario13x96.raw"
ampy put Mario13x96.raw /images/Mario13x96.raw
echo "Uploading MicroPython128x128.raw"
ampy put MicroPython128x128.raw /images/MicroPython128x128.raw
echo "Uploading MicroPythonW128x128.raw"
ampy put MicroPythonW128x128.raw /images/MicroPythonW128x128.raw
echo "Uploading Python41x49.raw"
ampy put Python41x49.raw /images/Python41x49.raw
echo "Uploading RaspberryPiWB128x128.raw"
ampy put RaspberryPiWB128x128.raw /images/RaspberryPiWB128x128.raw
echo "Uploading Rototron128x26.raw"
ampy put Rototron128x26.raw /images/Rototron128x26.raw
echo "Uploading Tabby128x128.raw"
ampy put Tabby128x128.raw /images/Tabby128x128.raw
echo "Uploading Tortie128x128.raw"
ampy put Tortie128x128.raw /images/Tortie128x128.raw
