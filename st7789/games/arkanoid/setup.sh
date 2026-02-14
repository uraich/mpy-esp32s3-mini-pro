#!/bin/bash
# This shell scripts sets up the picoweb server to run the Hello World
# WEB server. It uses picoweb to provide the Hello World WEB page.
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under GPL

echo "Setting Arkanoid levels"
dirs="$(ampy ls)"
echo $dirs

#check if /levels already exists

if [[ $dirs == *"/levels"* ]]
then
    echo "/levels directory already exists"
    echo "The following modules have been uploaded to /levels:"
    modules="$(ampy ls /levels)"
    for i in $modules ; do
	echo ${i#"/levels/"}
	done    
else
    echo "Creating /levels directory"
    ampy mkdir /levels
fi

echo ""
echo "Uploading Arkanoid levels"
echo "level 1"
ampy put levels/Level001.bin /levels/Level001.bin
echo "level 2"
ampy put levels/Level002.bin /levels/Level002.bin
echo "level 3"
ampy put levels/Level003.bin /levels/Level003.bin
echo "level 4"
ampy put levels/Level004.bin /levels/Level004.bin
echo "level 5"
ampy put levels/Level005.bin /levels/Level005.bin
echo "level 6"
ampy put levels/Level006.bin /levels/Level006.bin
echo "level 7"
ampy put levels/Level007.bin /levels/Level007.bin
echo "level 8"
ampy put levels/Level008.bin /levels/Level008.bin
echo "level 9"
ampy put levels/Level009.bin /levels/Level009.bin
