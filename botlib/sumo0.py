#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import ServoLib
import Button
import ProxLib


class Sumo:
    """The brains of the sumo bot"""

    # pins
    RSRV_PIN = 16
    LSRV_PIN = 18
    LED_PIN = 37
    BTN_PIN = 7
    PROX_TRIG_PIN = 11
    PROX_ECHO_PIN = 13
    RLN_PIN = 22
    LLN_PIN = 24

    # direction
    FWD = 0
    STOP = 1
    REV = 2

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Sumo.LED_PIN, GPIO.OUT)
        self.btn = Button.Button(Sumo.BTN_PIN, self.button_down)
        self.btn_pressed = False
        self.rsrv = ServoLib.Servo(Sumo.RSRV_PIN, 20, [1.3, 1.5, 1.7])
        self.lsrv = ServoLib.Servo(Sumo.LSRV_PIN, 20, [1.7, 1.5, 1.3])
        self.prox = ProxLib.HC_SR04(Sumo.PROX_TRIG_PIN, Sumo.PROX_ECHO_PIN)
        GPIO.setup(Sumo.RLN_PIN, GPIO.IN)
        GPIO.setup(Sumo.LLN_PIN, GPIO.IN)
        
    def shutdown(self):
        print 'shutdown'
        self.btn.cancel()
        self.rsrv.stop()
        self.lsrv.stop()
        time.sleep(0.5)
        GPIO.cleanup()

    def test(self):
        print 'test'
        self.led(1)

        self.btn_pressed = False
        while not self.btn_pressed:
            if self.line_detected(Sumo.LLN_PIN):
                self.rsrv.start(Sumo.REV)
                self.lsrv.start(Sumo.FWD)
                time.sleep(1.0)
                self.rsrv.start(Sumo.STOP)
                self.lsrv.start(Sumo.STOP)
            if self.line_detected(Sumo.RLN_PIN):
                self.rsrv.start(Sumo.FWD)
                self.lsrv.start(Sumo.REV)
                time.sleep(1.0)
                self.rsrv.start(Sumo.STOP)
                self.lsrv.start(Sumo.STOP)
        self.btn_pressed = False
        self.rsrv.stop()
        self.lsrv.stop()
        
        self.led(0)

    def led(self, state):
        GPIO.output(Sumo.LED_PIN, state)

    def toggle_led(self):
        GPIO.output(Sumo.LED_PIN, not GPIO.input(Sumo.LED_PIN))

    def button_down(self, pin):
        print "button_down"
        self.btn_pressed = True

    def line_detected(self, pin):
        """Line detector goes to low on white line"""
        if GPIO.input(pin):
            return False
        else:
            return True

    def line_evade(self, pin):
        self.rsrv.start(Sumo.REV)
        self.lsrv.start(Sumo.REV)
        time.sleep(0.3)
        if (pin == Sumo.RLN_PIN):
            self.rsrv.start(Sumo.FWD)
            self.lsrv.start(Sumo.REV)
        else:
            self.rsrv.start(Sumo.REV)
            self.lsrv.start(Sumo.FWD)
        time.sleep(1.5)
        self.rsrv.start(Sumo.STOP)
        self.lsrv.start(Sumo.STOP)

    def hunt(self):
        if self.prox.ping() < 75:
           self.lsrv.start(Sumo.FWD)
        else:
           self.lsrv.start(Sumo.REV)
        self.rsrv.start(Sumo.FWD)
        
    def crouch(self):
        print "crouch"
        self.btn.start()
        while not self.btn_pressed:
            self.toggle_led()
            time.sleep(1)
        self.btn_pressed = False

    def wrestle(self):
        print "wrestle start"
        self.led(1)
        self.btn_pressed = False
        
        while not self.btn_pressed:
            self.hunt()
            if (self.line_detected(Sumo.RLN_PIN)):
                self.line_evade(Sumo.RLN_PIN)
            if (self.line_detected(Sumo.LLN_PIN)):
                self.line_evade(Sumo.LLN_PIN)

        self.btn_pressed = False
        self.led(0)

if __name__ == "__main__":
    sumo = Sumo() # Init our sumobot
    sumo.crouch() # Wait for the button press
    #sumo.test() # Begin test
    time.sleep(1)
    sumo.wrestle() # Wrestle!
    sumo.shutdown()
