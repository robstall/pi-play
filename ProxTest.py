#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import SensorLib

GPIO.setmode(GPIO.BOARD)

prox = SensorLib.Prox(3, 5)

print("Started")

for i in range(0, 100):
    time.sleep(0.1)
    distance = prox.ping()
    print(distance)

GPIO.cleanup()

print('Complete')
