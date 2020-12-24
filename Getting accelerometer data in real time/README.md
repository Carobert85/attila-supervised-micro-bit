In this project I use the Micro:bit to investigate the motion of objects in real time. 
I attach one device to the moving object.If the program 'transmitter.py' has been uploaded to it, the Micro:bit gets the values of its accelerometer every 10 ms and sends it to the other one via radio.
The second Micro:bit is connected to a computer with Mu code editor. The program 'receiver.py' is running on the device and receives the data from the first one.
There are more options the handle the data.
1. Firstly, we can use the REPL and Plotter function of the MU editor to show the chnage of acceleration over time.
2. Another option is to stream the data to the MS Excel app using MS Data Streamer.
There are more options too that I am recenlty working on.
