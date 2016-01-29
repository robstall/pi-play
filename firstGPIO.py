import RPi.GPIO as GPIO
import time

print("Tick, Tick")

RED = 7
YELLOW = 11
GREEN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

for i in range(1, 61):
    if i < 21:
        GPIO.output(GREEN, i % 2)
    elif i < 41:
        GPIO.output(YELLOW, i % 2)
    else:
        GPIO.output(RED, i % 2)
    time.sleep(1)

GPIO.cleanup()    

print("Boom!")
