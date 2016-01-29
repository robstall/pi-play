#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

class Streetlight:
    OFF = 0
    GREEN = 1
    YELLOW = 2
    RED = 3
    RED_FLASHING = 4
    
    def __init__(self, redPin, greenPin, yellowPin):
        self.redPin = redPin
        self.greenPin = greenPin
        self.yellowPin = yellowPin
        GPIO.setup(redPin, GPIO.OUT)
        GPIO.setup(greenPin, GPIO.OUT)
        GPIO.setup(yellowPin, GPIO.OUT)

    def set_color(self, newColor):
        GPIO.output(self.redPin, 0)
        GPIO.output(self.greenPin, 0)
        GPIO.output(self.yellowPin, 0)
        if newColor == Streetlight.GREEN:
            GPIO.output(self.greenPin, 1)
        elif newColor == Streetlight.YELLOW:
            GPIO.output(self.yellowPin, 1)
        elif newColor == Streetlight.RED:
            GPIO.output(self.redPin, 1)


GPIO.setmode(GPIO.BOARD)

light = Streetlight(7, 13, 11)
light.set_color(Streetlight.GREEN)
time.sleep(2)
light.set_color(Streetlight.YELLOW)
time.sleep(2)
light.set_color(Streetlight.RED)
time.sleep(3)

GPIO.cleanup()    

