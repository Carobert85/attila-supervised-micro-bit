# Teaching the computer the distinguish different types of motion using supervised ML model and the BBC Micro:bit

The purpose of this project is to train a supervised ML model that can distinguish different motions. In this project I focus on the simple harmonic motion (SHM), the pendulum and the circular motion. The main stages of this project are listed below and the entire project is explained in details in an article mentioned at the end of the README.

## The data collection 
We attach a BBC Micro:bit (*transmitter*) to the moving object that collects data from its accelerometer. We get the acceleration along the x and y axes and we measure the angle of rotation around the z axis. The collected data is streamed via radio to another Micro:bit (*receiver*) that is connected to the main computer. The main computer gains the data from the receiver Micro:bit and writes it into a *.txt* file. *transmitter.py* and *receiver.py* are the programs running on the Micro:bits and *pc_ml_coll.py* or *pc_ml_test.py* programs run on the main computer to get the data and to write it to a file.

## Data processing
The data in the files are tuples of numbers and are in string format. Firstly, we need to convert the data into numeric format and to check if the data is in a good quality. This is essential if we want to train a good machine learning model.
*Visual check.ipynb* is a notebook that allows us to take a quick look at the data. We plot the acceleration values and the angle values against time and if the graphs are according to our expectations (at least visually), we can keep the file, otherwise we delete it.
Each experiment provides a long data file but to be able to train the ML algorithm, we need to create one single data instance to each experiment. We take the range of acceleration values along the x and y axes and the angle of rotation as well as the id of the motion into a tuple and add the tuple to a *pandas dataframe*. If we analyse the data of all successful experiment, we are going to have a data frame with 4 columns and as many rows as many succesful experiment we have. This dataset will be used to train and test the machine learning model. It is called *final_dataset.csv*. This work is done by *Managing_data.ipynb* notebook. 

## Training and testing the model
The main purpose of this project is to train a good *supervised machine learning model* that is able to categorise the test data instances and is able to distinguish the three types of motion. We chose 4 different algorithms (*SVM, decision tree, random forest, K-nearest*) to train on *final_dataset.csv* and to compare their performance. It is done in the *train_model.ipynb* file. After comparing the models' performance we chose the *K-nearest* model to test it live in the classroom. The *Live_test_final.ipynb* file is to carry out the live test. This is a short and complex notebook with only a few lines of code to make the live test easy. In this notebook we import lot of previously designed functions that are collected in *functions.py*.

For a more detailed description of the project, please check out the website accessed here: https://tmattila.wordpress.com/2022/04/05/machine-learning-to-everybody/

