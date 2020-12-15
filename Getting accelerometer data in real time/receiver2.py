from microbit import*
import radio
import utime

radio.on()
radio.config(group = 1)

while True:
    message = None
    while message is None:
        try:
            message = radio.receive()
            utime.sleep_ms(1)
            acc_z = int(message)
            print(acc_z)
        except ValueError:
            print('Cannot do it')
