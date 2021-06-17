from microbit import*

# pin0 and pin1 set to be 0 when starting the program
pin0.write_analog(0)
pin1.write_analog(0)

# define some variables that will be used when calculating the Planck constant 
speed_of_light = 3*10**8
wavelength = 6.4*10**(-7) # for a red LED. That value must be changed when using an LED with different colour
electron = 1.6*10**(-19)  # the charge of the electron
LED_const = 0.3431 # correction factor coming from the equation mentioned in readme

#starting the measurement with pressing button A
while True:
    if button_a.is_pressed():
        # to access to entire range of voltage, we should set number N to be 0<N<1024 but the output of the Micro:bit is not linear
        N = 480 # we start from the lower end of the linear characteristics
        pin0.write_analog(N)
        # check if there is any current through the LED
        current = pin1.read_analog()
        while True:
            if current<2: # we should set while current ==0, but it works better if we allow a very small current
                N += 1 # we increase the voltage if the current is negligible
                pin0.write_analog(N)
                current = pin1.read_analog()
                sleep_ms(100)
            
            else:
                N += 0
                # work out the value of the activation voltage
                activation_voltage = N*0.0114-4.2824
        
                # calculate the Planck-constant
                planck = (((electron * activation_voltage)-LED_const)*wavelength)/speed_of_light
                display.scroll(planck)
            break

# reset Micro:bit with pressing button B
while True:
    if button_b.is_pressed():
        pin0.write_analog(0)
        pin1.write_analog(0)
        
