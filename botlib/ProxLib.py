#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class HC_SR04:
    def __init__(self, triggerPin, echoPin):
        self.triggerPin = triggerPin
        self.echoPin = echoPin
        GPIO.setup(triggerPin, GPIO.OUT)
        GPIO.setup(echoPin, GPIO.IN)
        GPIO.output(triggerPin, GPIO.LOW)

    def ping(self):
        GPIO.output(self.triggerPin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, GPIO.LOW)

        startTime = time.time()
        signalOff = time.time()
        while GPIO.input(self.echoPin) == 0 and signalOff < startTime+0.1:
            signalOff = time.time()
            
        signalOn = time.time()    
        while GPIO.input(self.echoPin) == 1 and signalOn < signalOff+0.1:
            signalOn = time.time()
            
        distance = (signalOn - signalOff) * 17150
        
        return distance

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    prox = HC_SR04(11, 13)
    for i in range(0, 500):
        time.sleep(0.1)
        distance = prox.ping()
        print(round(distance, 2))
    GPIO.cleanup()
    

#RPi.GPIO.cleanup()
