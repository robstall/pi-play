#!/usr/bin/env python

import RPi.GPIO as GPIO
#import RPIO as GPIO
import time
import threading

class LED (threading.Thread):
   
   def __init__(self, pin):
      threading.Thread.__init__(self)
      self.pin = pin
      GPIO.setup(pin, GPIO.OUT)
      self.off()

   def setState(self, state):
      if not state:
         self.blinking = False
      GPIO.output(self.pin, state)

   def on(self):
      self.setState(GPIO.HIGH)

   def off(self):
      self.setState(GPIO.LOW)

   def blink(self, duration=1, delay=1):
      self.duration = duration
      self.delay = delay
      self.start()

   def run(self):
      print("Running...")
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.pin, GPIO.OUT)
      self.blinking = True
      while self.blinking:
         GPIO.output(self.pin, GPIO.HIGH)
         time.sleep(self.duration)
         if not self.blinking:
            break
         GPIO.output(self.pin, GPIO.LOW)
         time.sleep(self.delay)


# Testing...

GPIO.setmode(GPIO.BOARD)
led = LED(37)
print("Turn LED on for 3 seconds")
led.on()
count = 3
while count > 0:
   print(str(count))
   count = count - 1
   time.sleep(1)
print("Turn LED off")
led.off()
time.sleep(1)

print("Start LED blinking for five seconds...")
led.blink(0.25, 0.25)
count = 5
while count > 0:
   print(str(count))
   count = count - 1
   time.sleep(1)
print("Halting blinking")
led.off()

GPIO.cleanup()    
