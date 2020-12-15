from microbit import*
import radio
import utime

radio.on()
radio.config(group = 1)

while True:
  message = radio.receive() # the received message is a string
  utime.sleep_ms(1)
  acc_z = int(message) # convert the string to integer
  print(acc_z)
        
