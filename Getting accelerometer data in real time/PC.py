import serial
import time as t

# setting up and configure serial connection
serial = serial.Serial()
serial.baudrate = 115200
serial.port = "COM7"
serial.open()

start = t.time() # this is for setting up the length of the sampling preiod; this is the start time in the device's run time
while True:
    time = t.time()
    if time-start <5: # the sampling period is 5 seconds
        data = str(serial.readline()) # read the message from the Micro:bit
        # clean the string to be a triple of numbers
        data = data.strip("b'(" )
        data = data.strip(")\\r\\n'")
        
        #write the data into the file
        if data is not None:
            with open('collision.txt', 'a') as myfile: # the file collision.txt is prepared, so it must be opened 
                myfile.write(str(data)+'\n') # write the triple of numbers into the file
    
        print(data) # print the data on the screen in each iteration when running the code in the terminal
    else:
        quit() 
    
serial.close()
