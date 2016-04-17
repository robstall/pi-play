#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

for i in range(0, 10):
    GPIO.output(37, i % 2)
    time.sleep(1)

GPIO.cleanup()    
