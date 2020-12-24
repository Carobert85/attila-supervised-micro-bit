from microbit import*
import radio, utime

#configuring radio
radio.on()
radio.config(power = 7, group = 1)

#getting the data from the accelerometer and send it via radio
while True:
  utime.sleep_ms(10)
  accel = accelerometer.get_z() # get the data from the z-axis
  radio.send(str(accel)) # data type of sent message must be string
