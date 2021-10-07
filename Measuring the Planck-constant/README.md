# Measuring The Planck constant with an LED and Micro:bit

If we want to measure the Planck constant in the classroom the use of LEDs seems to be obvious. Lot of descriptions are available in this matter, I choose the article found in the link below: \
https://www.scienceinschool.org/2014/issue28/planck \
The crucial steps are: measuring and determining the threshold or activation voltage V<sub>a</sub> for LEDs with different colours, finding out or measuring the wavelength of the emitted light, plotting the graph V<sub>a</sub> against &lambda; and working out the gradient of the straight line of best fit (m) to calculate the Planck constant with the help of the following equation:\
h = em/c \
This method is useful and accurate enough but needs more time to carry out. I developed another method using Micro:bit to make the measurement faster so it can be used as a class demonstration, too. The arrangement of the experiment can be seen in Figure 1.

![Alt text](https://github.com/tmattila77/Microbit-projects/blob/main/Measuring%20the%20Planck-constant/figure%201.png "Figure 1")

The working principle is that Micro:bit increases the potential difference V across pin P0 and GND gradually, in small steps, from an initial voltage to the maximum. After every step Micro:bit measures the voltage V’ across pin P1 and GND to check if there is a current through the resistor R<sub>1</sub> and the LED. If V’ is 0 then Micro:bit increases V by 1 unit and this process continues until current starts flowing through the LED. When Micro:bit stops increasing V, the program stores the number of the last step and works out the activation voltage (V<sub>a</sub>) of the LED. Because without current the voltage across the LED must be the same as V, the voltage belonging to the last step can be considered to be the activation voltage. 

The Micro:bit has no digital analogue converter, so if we program a pin to be an analogue output the outcoming signal will be a PWM (Pulse Width Modulation) signal. This signal is not suitable for the measurement because the frequency of the signal is high, and we see the LED lighting for voltages lower then activation voltage, too. In fact, in this case the LED blinks faster than we were able to distinguish it from the continuous lighting. Therefore, we need to power the LED by a proper DC voltage, so we have to apply a low pass filter made of the resistor R<sub>0</sub> and the capacitor C (see Figure 1.). 
The circuit seen in the red rectangle behaves as a DC power source with adjustable output voltage.
Micro:bit has a 10 bit analogue digital converter, so in theory the resolution of the output voltage is 
3.1 V /2<sup>10</sup> = 3 mV.  

The characteristics of the analogue output of the Micro:bit can be seen in Figure 2. \

![Alt text](https://github.com/tmattila77/Microbit-projects/blob/main/Measuring%20the%20Planck-constant/figure%202.JPG "Figure 2")




