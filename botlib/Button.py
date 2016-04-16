#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import threading

class Button (threading.Thread):
   """Watches for states changes on a pin"""
   
   def __init__(self, pin, callback):
      threading.Thread.__init__(self)
      self.pin = pin
      self.cancelled = True
      self.callback = callback

   def cancel(self):
      self.cancelled = True

   def run(self):
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.pin, GPIO.IN)
      self.cancelled = False
      while not self.cancelled:
         time.sleep(0.05)
         self.callback(self.pin)
         #print str(self.cancelled) + ' ' + str(GPIO.input(self.pin))


# Testing...

def buttonPressed(pin):
   print 'button ' + str(pin) ' pressed'

if __name__ == "__main__":
   button = Button(7, buttonPressed)
   button.start()
   time.sleep(5)
   button.cancel()

