from microbit import*
import radio
import utime

# build up raddio connection and configure the radio network
radio.on()
radio.config(group = 1)

while True:
    message = radio.receive()
    utime.sleep_ms(10) # data is captured and processed in every 10 milliseconds
    
    # It often occurs that the transmitter device stops working due to the battery issues.
    # So, we have to check if the connection is living with the next snippet of code.
    # If the connection is live, the data type of the received message is 'str', 'None' otherwise.
    if type(message) == str:
        print(message)
        
    else:
        display.scroll('lost connection')
