"""
Utilizes ultrasonic sensor from the Elecfreaks IoT Kit to detect movement, 
adjusts smart bulbs to turn on/off based on location
"""

from microbit import *

distanceThresholdClosest = 200
distanceThresholdClose = 400
distanceThresholdFar = 600

ultrasonicPin = pin0
firstBulb = pin1
secondBulb = pin2
thirdBulb = pin3

while True:
    distance = ultrasonicPin.read_analog()

    if distance < distanceThresholdClosest:
        firstBulb.write_digital(1)
        secondBulb.write_digital(1)
        thirdBulb.write_digital(1)
    elif distance < distanceThresholdClose:
        firstBulb.write_digital(1)
        secondBulb.write_digital(1)
        thirdBulb.write_digital(0)
    elif distance < distanceThresholdFar:
        firstBulb.write_digital(1)
        secondBulb.write_digital(0)
        thirdBulb.write_digital(0)
    else:
        firstBulb.write_digital(0)
        secondBulb.write_digital(0)
        thirdBulb.write_digital(0)

    sleep(100)
