"""
Utilizes ultrasonic sensor from the Elecfreaks IoT Kit to detect movement, 
adjusts smart bulbs to turn on/off based on location
"""

from microbit import *

distanceThreshold = 260

ultrasonicPin = pin0
firstBulb = pin1
secondBulb = pin2

while True:
    distance = ultrasonicPin.read_analog()

    display.scroll(distance)

    if distance < distanceThreshold:
        firstBulb.write_digital(1)
        secondBulb.write_digital(1)
    elif distance > distanceThreshold:
        firstBulb.write_digital(0)
        secondBulb.write_digital(0)
    else:
        firstBulb.write_digital(0)
        secondBulb.write_digital(0)

    sleep(1000)
