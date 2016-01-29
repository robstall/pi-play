#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def ping(trigger, echo):
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)
    while GPIO.input(echo) == 0:
        signalOff = time.time()
    while GPIO.input(echo) == 1 or time.time() > signalOff + 200000:
        signalOn = time.time()
    distance = (signalOn - signalOff) * 17000
    return distance

GPIO.setmode(GPIO.BOARD)

pingIn = 38
pingOut = 40
GPIO.setup(pingOut, GPIO.OUT)
GPIO.setup(pingIn, GPIO.IN)

redPin = 7
GPIO.setup(redPin, GPIO.OUT)

for i in range(0, 600):
    time.sleep(0.1)
    distance = ping(pingOut, pingIn)
    print distance
    if distance <= 25:
        GPIO.output(redPin, GPIO.HIGH)
    elif distance > 25:
        GPIO.output(redPin, GPIO.LOW)

GPIO.cleanup()

