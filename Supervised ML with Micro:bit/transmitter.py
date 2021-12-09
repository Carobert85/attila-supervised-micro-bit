"""
This program runs on the Micro:bit attached to the moving object (transmitter). The purpose of this program is to collect data from the transmitter's accelerometer,
convert the digital data into scientific data (acceleration, measured in m/s<sup>2</sup> and transfer it to the receiver Micro:bit that is connected to the main compuetr.
"""

#importing libraries
from microbit import*
import radio
import utime
import math

#configuring radio
radio.on()
radio.config(power = 7, group = 1)

# the data acquisition lasts for 16 seconds, so I get the start time from the processor's running time
start = running_time()

radio.send("0, 0, 0") # this is the id of the motion. 0 stands for SHM, 1 for pendulum and 2 for circular motion

counter = 0 # I define this variable to count the iterations whilst collecting the data. counter is going to be sent to the main computer to help reading the data

# the data acquisition process
while True:
    time = running_time()-start # I define time of data collection using the processor's running time
    if time <16000: 
        utime.sleep_ms(50) # the data is collected in every 50 milliseconds
        
        # getting the digital data along x and y axes and converting them into real acceleration values. Working out the value of rotion as well
        accel_x = round((9.81/1024)*accelerometer.get_x(), 2) # acceleartion along the x-axis
        accel_y = round((9.81/1024)*accelerometer.get_y(), 2) # acceleration along the y-axis
        angle = round(math.atan2(accel_x, accel_y),2) # work out the angle of rotation
        
        # sending the data via radio
        send = (accel_x, accel_y, angle) # the tuple that is going to be sent to the main computer
        radio.send(str(counter))
        radio.send(str(send))
        counter+=1
    else:
        radio.off()
        while True:
            display.scroll("restart me")




