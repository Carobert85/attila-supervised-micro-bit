from microbit import*
import radio
import utime

radio.on()
radio.config(group = 1)

while True:
    message = radio.receive()
    utime.sleep_ms(10)
    # Often occurs that transmitter device stops working due to the battery issues.
    #So, we have to check if the connection is living with the next snippet of code.
    # If there is connection, the data type of the received message is 'str', 'None' otherwise.
    
    if type(message) == str:
        accel_z = int(message)
        accel_z = (9.81/1024)*accel_z # turn the number provided by the AD converter to the real value of acceleration in m/s**2
        to_print = (0,0,accel_z) # set up a tuple to help the plotter of Mu to work
        print(to_print)
        
    else:
        print('I lost the connection with the transmitter')
