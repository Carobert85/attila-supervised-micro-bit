"""
This program runs on the receiver Micro:bit attached to the main computer. The purpose of this code is to receive the data sent by the transmitter Micro:bit via radio
and to sent it to the computer to be saved into a .txt file. In case of disruption in the radio connection, the receiver device sends an error message to the user.
"""

# importing files
from microbit import*
import radio
import utime

#configuring radio connection
radio.on()
radio.config(group = 1)

#checking radio connection and transfer the received data to the main computer.
# If there is a connection between the transmitter and the receiver devices, the data type of the received message is 'str', 'None' otherwise.

while True:
    message = radio.receive()
   
    if type(message) == str:
        print(message)

    else:
        display.scroll('lost connection')
