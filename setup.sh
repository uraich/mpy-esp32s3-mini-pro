#!/bin/bash
# This shell scripts sets up the picoweb server to run the Hello World
# WEB server. It uses picoweb to provide the Hello World WEB page.
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under GPL

echo "Setting up the hardware file for the esp32s3_mini_pro"
dirs="$(ampy ls)"
echo $dirs

#check if /lib already exists

if [[ $dirs == *"/lib"* ]]
then
    echo "/lib directory already exists"
    echo "The following modules have been uploaded to /lib:"
    modules="$(ampy ls /lib)"
    for i in $modules ; do
	echo ${i#"/lib/"}
	done    
else
    echo "Creating /lib directory"
    ampy mkdir /lib
fi

echo ""
echo "Uploading hw_esp32s3_mini_pro.py"
ampy put hw_esp32s3_mini_pro.py /lib/hw_esp32s3_mini_pro.py
echo "Uploading the display driver st7789py.py"
ampy put st7789py/st7789py.py /lib/st7789py.py
echo "Upload the display configurator"
ampy put st7789py/st7789_config.py /lib/st7789_config.py
