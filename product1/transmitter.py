from microbit import *

import radio
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('light_on')
    elif button_b.is_pressed():
        radio.send('light_off')
        
    sleep(100)
