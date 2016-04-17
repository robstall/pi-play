#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import threading

class Button (threading.Thread):
   """Watches for states changes on a pin"""
   
   def __init__(self, pin, callback):
      """Init with pin and button down callback"""
      threading.Thread.__init__(self)
      self.pin = pin
      self.normal = GPIO.LOW
      self.state = self.normal
      self.cancelled = True
      self.callback = callback

   def set_normal_state(self, normal):
      """Normal is the pin value when not pressed"""
      self.normal = normal

   def cancel(self):
      """Stop watching the button"""
      self.cancelled = True

   def run(self):
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.pin, GPIO.IN)
      time.sleep(1) # Need to give the pin a chance to settle
      self.cancelled = False
      timeunlatch = time.clock()
      while not self.cancelled:
         time.sleep(0.05)
         timenow = time.clock()
         pinstate = GPIO.input(self.pin)
         print(pinstate, self.state, self.normal, timenow, timeunlatch)
         if (pinstate != self.state and timenow > timeunlatch):
            timeunlatch = timenow + 0.01
            self.state = pinstate
            if self.state != self.normal:
               self.callback(self.pin)
               print "button down", self.pin


# Testing...

def buttonPressed(pin):
   print 'button ' + str(pin) + ' pressed'

if __name__ == "__main__":
   button = Button(7, buttonPressed)
   button.start()
   time.sleep(10)
   button.cancel()

