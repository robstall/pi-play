#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import ServoLib


class Sumo:
    """The brains of the sumo bot"""

    # pins
    RSRV_PIN = 16
    LSRV_PIN = 18
    LED_PIN = 37

    # direction
    FWD = 0
    STOP = 1
    REV = 2

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Sumo.LED_PIN, GPIO.OUT)
        self.rsrv = ServoLib.Servo(Sumo.RSRV_PIN, 20, [1.3, 1.5, 1.7])
        self.lsrv = ServoLib.Servo(Sumo.LSRV_PIN, 20, [1.7, 1.5, 1.3])
        
    def shutdown(self):
        GPIO.cleanup()

    def test(self):
        self.blink_led()
        
        # Run right servo
        self.rsrv.start(Sumo.FWD)
        time.sleep(1)
        self.rsrv.stop()

        # Run left servo
        self.lsrv.start(Sumo.FWD)
        time.sleep(1)
        self.lsrv.stop()

        self.blink_led()

    def blink_led(self):
        GPIO.output(Sumo.LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(Sumo.LED_PIN, GPIO.LOW)
    

if __name__ == "__main__":
    sumo = Sumo()
    sumo.test()
    sumo.shutdown()
