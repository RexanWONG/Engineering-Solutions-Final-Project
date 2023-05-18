from microbit import *

# Set up radio
import radio
radio.on()

ledPin = pin0

while True:
    message = radio.receive()
    
    if message:
        if message == 'light_on':
            ledPin.write_digital(1)
            
        elif message == 'light_off':
            ledPin.write_digital(0)
