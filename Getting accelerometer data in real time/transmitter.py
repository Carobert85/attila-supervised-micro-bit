from microbit import*
import radio
import utime

#configuring radio
radio.on()
radio.config(power = 7, group = 1)

#getting the data from the accelerometer and send it via radio
#I convert the digital data provided by the device into real acceleration values and round it to floats with 2 decimal places 
while True:
    utime.sleep_ms(1)
    accel_x = round((9.81/1024)*accelerometer.get_x(), 2) # get and convert the data along the x-axis
    accel_y = round((9.81/1024)*accelerometer.get_y(), 2) # get and convert the data along the y-axis
    accel_z = round((9.81/1024)*accelerometer.get_z(), 2) # get and convert the data along the z-axis
    accel = (accel_x, accel_y, accel_z)
    radio.send(str(accel))
