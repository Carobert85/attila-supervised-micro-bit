"""
The purpose of this code is to measure your reaction time.
When you see the happy face, press button A immediatelly. Your reaction time is going to be displayed in milliseconds.
You have three tries but be careful, the image gets fainter each time.
At the end you will see your average reaction time.
Good luck!
"""

# importing libraries
from microbit import *
import random
import utime

display.scroll('Press button A when you see the happy face!')

# I design the happy faces in different brightness and put them into a list
image1 = Image("00000:09090:00000:90009:09990")
image2 = Image("00000:06060:00000:60006:06660")
image3 = Image("00000:03030:00000:30003:03330")
images = [image1, image2, image3]

sum_ = 0 # I define this variable to help working out the average value at the end
for i in range(3): # you have 3 tries
    reaction = 0 # initialize the reaction time variable

    # the image is going to appear randomly between 0 and 10 seconds
    time = random.randint(0,10)
    display.scroll(str(i+1)) # the number of try
    display.clear()
    utime.sleep(time)

    # image appears, start to measure the reaction time
    display.show(images[i])
    start = running_time()

    # press button A and the measurement of the reaction time will stop
    while True:
        if button_a.is_pressed():
            stop = running_time()
            reaction = stop - start

            #display reaction time and clear screen
            display.scroll(reaction)
            sum_+= reaction # increase the sum of the measured reaction times with the current value
            display.clear()
            break


# work out and display the average reaction time
average = round(sum_/3, 2)
display.scroll(average)

