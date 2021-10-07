The most exciting application of an accelerometer is to observe a moving object in real time and to collect numerical data of its motion. Unfortunately, the Micro:bit does not have an internal permanent memory where the gained data could be stored. However, there are some simple solutions to gain the data collected by Micro:bit and to record them. One of them is the Excel Data Streamer. Data Streamer is a freely downloadable application for Microsoft Excel that enables the user to read out data from a sensor through a microcontroller or send out data to an actuator in real time. BBC Micro:bit is also suitable for helping data transfer from a sensor to the Excel worksheet making it possible to visualize and analyse the gathered data. One of the Micro:bit’s advantage is that we can collect data from the inbuilt sensors, in my example from the accelerometer.

I observed the motion of a long (l = 2.36 m) pendulum with Micro:bit and Data Streamer. I attached the board computer to the top of the moving object and programmed it to measure and stream via radio the value of az during the time of the observation. The streamed data was captured by a receiver Micro:bit which sent it to the Excel. (Figure 1.) The programs for both devices can be investigated in this repo and a portion of the results in Figure 2.


The second Micro:bit is connected to a computer with Mu code editor. The program 'receiver.py' is running on the device and receives the data from the first one.
There are more options the process the data.
1. Firstly, we can use the REPL and Plotter function of the MU editor to show the chnage of acceleration over time.
2. Another option is to stream the data to the MS Excel app using MS Data Streamer.

I am currently working on a program that can be run on the PC and which writes the data captured by the second Micro:bit into a csv file. My goal is to design a ipynb file that can access the data from the csv file to do further investigations to the data. More difficult motions, collisions etc. can be deeper analysed by using the notebook. 
