#/bin/usr/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)

for n in range(0, 150):
    time.sleep(.3)
    print GPIO.input(36)

GPIO.cleanup()
