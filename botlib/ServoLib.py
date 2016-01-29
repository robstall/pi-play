#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

class Servo:
   def __init__(self, pin, cycle_ms, pulse_ms_list):
      self.pin = pin
      self.frequency = 1000 / cycle_ms
      self.dutycycles= []
      for p in pulse_ms_list:
         self.dutycycles.append(p / cycle_ms * 100)
      print "Servo: " + self.description()
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.pin, GPIO.OUT)
      self.pwm = GPIO.PWM(self.pin, self.frequency)

   def start(self, idx):
      self.pwm.ChangeDutyCycle(self.dutycycles[idx])
      self.pwm.start(self.dutycycles[idx])

   def stop(self):
      self.pwm.stop()

   def description(self):
      return "pin=" + str(self.pin) + " freq=" + str(self.frequency) + " dutycycles=" + str(self.dutycycles)

if __name__ == "__main__":
   servo = Servo(7, 20, [1.3, 1.5, 1.7])

   servo.start(0)
   time.sleep(3)

   servo.start(1)
   time.sleep(3)

   servo.start(2)
   time.sleep(3)

   servo.stop()

   GPIO.cleanup()
    
