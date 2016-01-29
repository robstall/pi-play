#!/usr/bin/python

import RPi.GPIO, time

class HC_SR04:
    def __init__(self, triggerPin, echoPin):
        self.triggerPin = triggerPin
        self.echoPin = echoPin
        RPi.GPIO.setup(triggerPin, RPi.GPIO.OUT)
        RPi.GPIO.setup(echoPin, RPi.GPIO.IN)
        RPi.GPIO.output(triggerPin, RPi.GPIO.LOW)
        print "Waiting for HC-SRO4 sensor to settle"
        time.sleep(2)
        print "Complete"

    def ping(self):
        RPi.GPIO.output(self.triggerPin, RPi.GPIO.HIGH)
        time.sleep(0.00001)
        RPi.GPIO.output(self.triggerPin, RPi.GPIO.LOW)

        startTime = time.time()
        signalOff = time.time()
        while RPi.GPIO.input(self.echoPin) == 0 and signalOff < startTime+0.1:
            signalOff = time.time()
            
        signalOn = time.time()    
        while RPi.GPIO.input(self.echoPin) == 1 and signalOn < signalOff+0.1:
            signalOn = time.time()
            
        distance = (signalOn - signalOff) * 17150
        
        return distance

if __name__ == "__main__":
    RPi.GPIO.setmode(RPi.GPIO.BOARD)
    prox = HC_SR04(3, 7)
    for i in range(0, 100):
        time.sleep(0.1)
        distance = prox.ping()
        print(round(distance, 2))
    RPi.GPIO.cleanup()
    

#RPi.GPIO.cleanup()
