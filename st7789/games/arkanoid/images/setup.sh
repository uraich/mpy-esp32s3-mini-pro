#!/bin/bash
# This shell scripts sets up the picoweb server to run the Hello World
# WEB server. It uses picoweb to provide the Hello World WEB page.
# Demo program for the course on the Internet of Things (IoT) at the
# University of Cape Coast (Ghana)
# Copyright (c) U. Raich April 2020
# This program is released under GPL

echo "Uploads the Arkanoid image files to /images"
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
echo "Uploading Arkanoid_Border128x118.raw"
ampy put Arkanoid_Border128x118.raw images/Arkanoid_Border128x118.raw
echo "Uploading Ball7x7.raw"
ampy put Ball7x7.raw /images/Ball7x7.raw
echo "Uploading blinka45x48.raw"
ampy put Brick_Blue13x7.raw /images/Brick_Blue13x7.raw
echo "Uploading Brick_Green13x7.raw"
ampy put Brick_Green13x7.raw /images/Brick_Green13x7.raw
echo "Uploading Brick_Pink13x7.raw"
ampy put Brick_Pink13x7.raw /images/Brick_Pink13x7.raw
echo "Uploading Brick_Red13x7.raw"
ampy put Brick_Red13x7.raw /images/Brick_Red13x7.raw
echo "Uploading Brick_Yellow13x7.raw"
ampy put Brick_Yellow13x7.raw /images/Brick_Yellow13x7.raw
echo "Uploading Paddle12x4.raw"
ampy put Paddle12x4.raw /images/Paddle12x4.raw
echo "Uploading Paddle25x8.raw"
ampy put Paddle25x8.raw /images/Paddle25x8.raw
echo "Uploading Pi16x16.raw"
ampy put Pi16x16.raw /images/Pi16x16.raw

