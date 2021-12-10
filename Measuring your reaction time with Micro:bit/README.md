# Measuring reaction time with BBC Micro:bit

In the Physics curriculum reaction time and road safety is an important topic. Although many apps can be downloaded to test somebody's reaction time, creating our own ones
and understand the working principles of those apps is vital. That was the reason I designed this short code for students.

### The main steps when testing reaction time
1. Generate a time interval randomly between 0 and 10 s. Stop the code running for this interval.
2. Display an image (a happy face) on the LED screen and start measuring the time (read the device running time in milliseconds)
3. User presses button A so time measurement stops. (read the device running time again)
4. Take the difference of the running times (stop - start). This is the reaction time in milliseconds that will be displayed to the user.

### Extras in my program
1. The user has 3 attempts and Micro:bit calculates the mean of the measured reaction times.
2. In each turn, the image is getting fainter to test the user's sensation.

