"""
This program runs on the Micro:bit attached to the moving object. The purpose of this code is to collect data from the device's accelerometer every 50ms, 
convert the digital data into scientific (from integers between 0-1023 to acceleration measured in m/s<sup>2</sup> ) and send it to the receiver Micro:bit 
via radio signal. The sent data is in string format and is a tuple of 3 numbers: acceleration along x-axis, acceleration along y-axis, and the tilt angle along z-axis. 
"""

# importing libraries
from microbit import*
import radio
import utime
import math

#configuring radio
radio.on()
radio.config(power = 7, group = 1)

# the time of data collection is 16 s. Set the start time as
start = running_time()

# Micro:bit sends the id of the motion
radio.send("1, 0, 0") # 0 stands for SHM, 1 for pendulum and 2 for circular motion in the first character

#We define a counter that will be sent to the main computer in each iteration. This will help the computer to control the process of data acquisition.
counter = 0

# Collect and send the data from the accelerometer for 16 seconds
while True:
    time = running_time()-start
    if time <16000:
        utime.sleep_ms(50) # the data is collected in every 50 milliseconds
        #I convert the digital data provided by the sensor into real acceleration values and round it to floats with 2 decimal places
        accel_x = round((9.81/1024)*accelerometer.get_x(), 2) # get and convert the data along the x-axis
        accel_y = round((9.81/1024)*accelerometer.get_y(), 2) # get and convert the data along the y-axis

        # SHM: angle = arctan(accel_y/accel_x), pendulum and circular: angle = arctan(accel_x/accel_y). The difference is due to the positioning of the Micro:bit attached to the object.
        angle = round((math.atan2(accel_x, accel_y)*180/math.pi),2)
        send = (accel_x, accel_y, angle)
        radio.send(str(counter))
        radio.send(str(send))
        counter+=1
    else:
        # stop sending data and turn off radio. Wait for restart.
        radio.off()
        while True:
            display.scroll("restart me")
