"""
The purpose of this file is similar to the purpose of <i>pc_ml_coll.py</i>. Everything in its preliminary description and in the comments applies here, too. 
The difference is that we use this code to collect data when testing the trained machine learning model in the classroom live. Because we would like to have the
test data instance in a different directory from the train data instances, we move the test data instance from the original directory (source_dir) to its final
directory (target_dir).
"""

# importing libraries
import serial
import time
import os
import shutil

# adding source and target directories to move the test data instance
source_dir = 
target_dir =

# setting up and configuring the serial connection
serial = serial.Serial()
serial.baudrate = 115200
serial.port = "COM3"
serial.open()


# collecting data from the receiver device, clearing it from additional characthers and writing it to a text file
print("Let's start the experiment!")
iteration = 0
while True:
    while True:
        data = str(serial.readline())
        
        # clear the data from additional characters
        data = data.strip("b'(" )
        data = data.strip(")\\r\\n'")
        
        #filter iteration data (won't be written into the file) from motion data
        if len(data)<4:
            iteration+=1
            print("iteration: ", iteration)
            
        # if this is the last tuple, write it to the file and move the file to its final target directory
        if len(data)>4 and iteration==300:
            with open('Live_test.txt', 'a') as myfile:
                myfile.write(str(data)+'\n')
            print(data)
            print('Data collection has ended.')
            # move the file
            time.sleep(1.0)
            file_names = os.listdir(source_dir)
            for file_name in file_names:
                if file_name == 'Live_test.txt':
                    shutil.move(os.path.join(source_dir, file_name), target_dir)
            quit()
            
        # if this is not the last tuple, write it into the file
        else:
            if len(data)>4:
                with open('Live_test.txt', 'a') as myfile:
                    myfile.write(str(data)+'\n')
                    print(data)
                    
  # close the serial connection at the end of the data collection
  serial.close()
