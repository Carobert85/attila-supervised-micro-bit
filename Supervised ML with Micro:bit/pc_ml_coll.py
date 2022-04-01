"""
This program is running on the main computer whilst collecting data with the Micro:bits. Its main purpose is to 
- gain the data directly from the receiver device;
- clear it from additional characters and turn it into a tuple of three numbers and
- write the data into a text file line by line.
After running this code, we are going to gain a text file containing the tuples for each experiment. 
Each tuple is a single string so the file cannot be considered to be a csv file.
"""

# importing the serial library
import serial

# setting up and configuring the serial connection
serial = serial.Serial()
serial.baudrate = 115200
serial.port = "COM3"
serial.open()


# receiving the data from the receiver Micro:bit, transforming it and writing it to file 
number = input("What was the number of the last sample?") # for a continuous data collection, we don't need to restart the program just to create a new file with one bigger id number
counter = int(number) + 1
iteration = 0
while True:
    while True:
        data = str(serial.readline())
        
        # clean the data from additional characters
        data = data.strip("b'(" )
        data = data.strip(")\\r\\n'")
        
        # Iteration is a short string (up to 3 characters). Iteration will not be written to file.
        if len(data)<4:
            iteration+=1
            print("iteration: ", iteration)
            
        # The tuples are longer strings. If this is the last tuple coming from the receiver device, stop the data collection and finish writing the file. 
        if len(data)>4 and iteration==300:
            with open('MLtest'+str(counter)+'.txt', 'a') as myfile:
                myfile.write(str(data)+'\n')
            print(data)
            new = input("Do you want to take a new measurement? y/n")
            if new == "y":
                counter+=1
                iteration = 0
                break
            else:
                quit()
        
        # If this is not the last tuple from the receiver device, write it to the file.
        else:
            if len(data)>4:
                with open('MLtest'+str(counter)+'.txt', 'a') as myfile:
                    myfile.write(str(data)+'\n')
                    print(data)
    
# Close serial connection at the end of the data collection.        
serial.close()
