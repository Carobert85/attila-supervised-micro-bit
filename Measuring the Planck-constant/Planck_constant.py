from microbit import*

# pin0 and pin1 set to be 0 when launching Micro:bit
pin0.write_analog(0)
pin1.write_analog(0)

# define some variables
speed_of_light = 3*10**8
wavelength = 6.4*10**(-7) # for a red LED
electron = 1.6*10**(-19)  # the charge of the electron
LED_const = 0.3431

#starting the measurement with pressing button A
while True:
    if button_a.is_pressed():
        # to access to entire range of voltage, we can set number N to be 0<N<1024
        N = 480 # we start from the start of the linear characteristics
        pin0.write_analog(N)
        current = pin1.read_analog() # check the circuit for current
        while current<2: # we should set while current ==0, but it works better if we allow a very small current
            N += 1 # we increase the voltage if the current is negligible
            pin0.write_analog(N)
            current = pin1.read_analog()
            sleep_ms(100)
        
        # work out the value of the activation voltage
        activation_voltage = N*0.0114-4.2824
        
        # calculate the Planck-constant
        planck = (((electron * activation_voltage)-LED_const)*wavelength)/speed_of_light
        display.scroll("Planck_constant:", planck, "Js")
    break

# reset Micro:bit with pressing button B
while True:
    if button_b.is_pressed():
        pin0.write_analog(0)
        pin1.write_analog(0)
        
