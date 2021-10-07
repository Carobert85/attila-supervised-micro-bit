In this project I use the Micro:bit to investigate the motion of objects in real time. 
I attach one device to the moving object with the program 'transmitter.py' uploaded. The Micro:bit gets the values of its accelerometer every 10 ms and sends it to the second one via radio.
The second Micro:bit is connected to a computer with Mu code editor. The program 'receiver.py' is running on the device and receives the data from the first one.
There are more options the process the data.
1. Firstly, we can use the REPL and Plotter function of the MU editor to show the chnage of acceleration over time.
2. Another option is to stream the data to the MS Excel app using MS Data Streamer.

I am currently working on a program that can be run on the PC and which writes the data captured by the second Micro:bit into a csv file. My goal is to design a ipynb file that can access the data from the csv file to do further investigations to the data. More difficult motions, collisions etc. can be deeper analysed by using the notebook. 
