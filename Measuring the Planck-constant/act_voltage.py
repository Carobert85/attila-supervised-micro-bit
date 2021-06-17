from microbit import*

# pin0 and pin1 set to be 0 when starting Micro:bit
pin0.write_analog(0)
pin1.write_analog(0)

#starting the measurement with pressing button A
while True:
    if button_a.is_pressed():
        # to access to entire range of voltage, we can set number N to be 0<N<1024 but the output is not linear
        N = 480 # we start from the lower and of the linear characteristics
        pin0.write_analog(N)
        # check if there is any current flowing through the LED
        current = pin1.read_analog()
        while True:
            if current<2: # we should set while current ==0, but it works better if we allow a very small current
            N += 1 # we increase the voltage if the current is negligable
            pin0.write_analog(N)
            current = pin1.read_analog()
            sleep_ms(100)
            
         else:
            # work out the value of the activation voltage
            activation_voltage = N*0.0114-4.2824
            activation_voltage.round(2)
            #display the activation voltage in Volts
            display.scroll(activation_volatge)
        
        break
        
        
# reset Micro:bit with pressing button B
while True:
    if button_b.is_pressed():
        pin0.write_analog(0)
        pin1.write_analog(0)
        



