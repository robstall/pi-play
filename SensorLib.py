#!/usr/bin/python

import RPi.GPIO, time

class Prox:
    def __init__(self, triggerPin, echoPin):
        self.triggerPin = triggerPin
        self.echoPin = echoPin
        RPi.GPIO.setup(triggerPin, RPi.GPIO.OUT)
        RPi.GPIO.setup(echoPin, RPi.GPIO.IN)

    def ping(self):
        RPi.GPIO.output(self.triggerPin, RPi.GPIO.HIGH)
        time.sleep(0.00001)
        RPi.GPIO.output(self.triggerPin, RPi.GPIO.LOW)
        signalOff = time.time()
        while RPi.GPIO.input(self.echoPin) == 0:
            signalOff = time.time()
        while RPi.GPIO.input(self.echoPin) == 1 or time.time() > signalOff + 200000:
            signalOn = time.time()
        distance = (signalOn - signalOff) * 17000
        return distance

#class LED:
#    def __init__(self):

RPi.GPIO.setmode(RPi.GPIO.BOARD)   
prox = Prox(38, 40)
print(str(prox.ping()))

RPi.GPIO.cleanup()
