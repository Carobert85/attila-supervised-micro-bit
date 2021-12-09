# -*- coding: utf-8 -*-
"""
This program runs on the main computer. The puropse of this program is to collect data from the receiver Micro:bit, to process it and to write it to a .txt file.
This file is going to be opened by *Managing_data.ipynb* and the data will undergo further procession.
"""

#importing serial library and configuring serial connection
import serial

serial = serial.Serial() # I create serial object
serial.baudrate = 115200 # I define Baud rate
serial.port = "COM3" # I define the port 
serial.open() # open serial connection


# We are going to create lot of files that have their own id numbers. If we take a brake we can carry on running the two lines of code below. 
number = input("What was the number of the last sample?")
file_id = int(number) + 1

iteration = 0 # this variable is for counting the iterations whilst collecting the data and writing the file
while True:
    while True:
        data = str(serial.readline()) # data received from the receiver Micro:bit
        
        # The form of the data is b'(" the triple of numbers ")\\r\n'. We need to clean the data from the charachters before and after the triple of numbers.
        data = data.strip("b'(" )
        data = data.strip(")\\r\\n'")
        
        # The data can be the number of iteration sent by the transmitter Micro:bit (its length is less than 4) or the triple of number (its length is longer than 4).
        
        # Fisrtly, we find out if the data is the number of iteration. If yes, the program prints onto the screen but does not write to the file.
        if len(data)<4:
            iteration+=1
            print("iteration: ", iteration)
            
        # We find out wheter the data is the triple of numbers and if it is the last. If yes, the program writes the data to the file and asks if we want to run it again.
        if len(data)>4 and iteration==308:
            with open('MLtest'+str(file_id)+'.txt', 'a') as myfile:
                myfile.write(str(data)+'\n')
            print(data)
            new = input("Do you want to take a new measurement? y/n")
            if new == "y":
                counter+=1
                iteration = 0
                break
            else:
                quit() # if we don't want to run the code again, it stops.
        
        # if the data is the triple of numbers but not the last one, the program writes it to the file.
        else:
            if len(data)>4:
                with open('MLtest'+str(file_id)+'.txt', 'a') as myfile:
                    myfile.write(str(data)+'\n')
                    print(data)
    
            
       
# If the program stops, close the serial connection.       
serial.close()
    
