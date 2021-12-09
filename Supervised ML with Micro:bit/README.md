# Teaching the computer the distinguish different types of motions using supervised ML model and the BBC Micro:bit
### (ongoing project)

The purpose of this project is to train a supervised ML model that can distinguish different types of motions. In this project I focus on simple harmonic motion (SHM), pendulum and circular motion. 

## The data collection 
I attach a BBC Micro:bit (*transmitter*) to the moving object and collect data from its accelerometer. We get the acceleration along the x and y axes and we measure the angle of rotation around the z axis. The data collected will be streamed via radio to another Micro:bit (*receiver*) that is connected to the main computer. The main computer gains the data from the receiver Micro:bit and writes it into a *.txt* file. *transmitter.py* and *receiver.py* are the programs running on the Micro:bits and *PC_program.py* runs on the main computer to get the data and write it to the files.

## Data processing
The data in the files are triples of numbers and are in string format. Firstly, we need to convert the data into numeric format and check if the data is in good quality. This is essential if we want to train a machine learning algorithm.
*Visual check.ipynb* is a notebook that allows us to take a quick look at the data. We plot the acceleration values and the angle values against time and if the graphs are according to our expectations (at least visually), we can keep the file, otherwise we delete the file with wrong data quality.
Each experiment provides a long data file but to be able to run the ML algorithm, we need to create one single data to each experiment. We put the range of acceleration values along x and y axes and the angle of rotation as well as the id of the motion into a tuple and add it to a *pandas dataframe*. If we analyse the data of all successful experiment, we are going to have a data frame with 4 columns and as many rows as many succesful experiment we had. This dataset will be used to train and test the machine learning model.

## This is where I am with this project, I am currently working on it.
