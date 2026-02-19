# qmi8658_demo.py: a test program based on the wemos qmi8658 driver
# Copyright (c) U.Raich, 19. Feb.2026
#
# Released under the MIT license

from time import sleep_ms
from machine import I2C
from qmi8658 import QMI8658

# try to import the hardware definition file
import sys
try:
    from hw_esp32s3_mini_pro import *
except:
    print("Please make sure hw_esp32s3_mini_pro.py has been uploaded to /lib")
    sys.exit()

i2c = I2C(1,scl=SCL,sda=SDA)
qmi8658 = QMI8658(i2c)

# the driver has no method to find out if new data are available
# I read every 500 ms
print("acc x,y,z")
try:
    for i in range(100):
        # the driver returns a tuple of x,y,z values
        gyro_data = qmi8658.read_gyro()
        acc_data  = qmi8658.read_accel()
        # print the accelerometer data
        print("{:5.3f},{:5.3f},{:5.3f},".format(
            acc_data[0],acc_data[1],acc_data[2]))
        # You may want to uncomment the two lines below
        # and comment the 2 lines above, to display only the
        # gyroscope data
        # print("{:5.3f},{:5.3f},{:5.3f},".format(
        #     gyro_data[0],gyro_data[1],gyro_data[2]))
        sleep_ms(100)
except KeyboardInterrupt:
    pass
