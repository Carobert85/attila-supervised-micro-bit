"""
This program runs on a Micro:bit connected to the main computer (receiver). The purpose of this program is to collect data sent via radio by the other Micro:bit attached
to the moving object transmitter) and transfer it to the main computer. There is no data processing done at this stage.
"""
# importing libraries
from microbit import*
import radio
import utime

# configuring radio
radio.on()
radio.config(group = 1)

# the data collection and transfer
while True:
    message = radio.receive() # data received via radio from the transmitter
    
    """
    It often occurs that transmitter device stops working due to battery issues.
    Hence, we have to check if the connection is living with the next snippet of code.
    If there is connection, the data type of the received message is 'str', 'None' otherwise.
    """
    
    if type(message) == str:
        print(message)

    else:
        display.scroll('lost connection')


