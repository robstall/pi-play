#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

for n in range(0, 150):
    time.sleep(.3)
    print GPIO.input(8)

GPIO.cleanup()
