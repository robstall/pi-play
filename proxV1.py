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

RED = 7

GREEN = 33

YELLOW = 11

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

for i in range(0, 100):
    time.sleep(0.25)
    distance = ping(pingOut, pingIn)
    print distance
    if distance <= 40:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)
    elif distance > 40 and distance <= 75:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
    elif distance > 75:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(GREEN, GPIO.HIGH)
    
GPIO.cleanup()

print("Complete")

