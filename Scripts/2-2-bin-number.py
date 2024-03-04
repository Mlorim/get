import RPi.GPIO as GPIO
import time
import random as rd

dac = [8, 11, 7, 1, 0, 5, 12, 6]
# number = [rd.choice([0, 1]) for i in range(len(dac))] 
number = [0] * 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number) 
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()
