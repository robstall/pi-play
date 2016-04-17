#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.IN)

for n in range(0, 250):
    time.sleep(.3)
    print n, 22, GPIO.input(22), 24, GPIO.input(24)

GPIO.cleanup()
