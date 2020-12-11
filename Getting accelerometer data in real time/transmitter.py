from microbit import*
import radio

#configuring radio
radio.on()
radio.config(power = 7, group = 1)

#getting the data from the accelerometer and send it via radio
sleep_ms(1)
accel = accelerometer.get_z() # get the data from the z-axis
radio.send_number(accel))
