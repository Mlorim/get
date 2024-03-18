import RPi.GPIO as GPIO
import time


dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def to_bin(i):
    return [int(j) for j in bin(i)[2:].zfill(8)]


try:
    T = int(input())
    t = T/(256 + 255)
    while True:
        for i in range(0, 256):
            GPIO.output(dac, to_bin(i))
            print(i)
            time.sleep(t)
        for i in range(254, -1, -1):
            GPIO.output(dac, to_bin(i))
            print(i)
            time.sleep(t)
finally:
    GPIO.cleanup()
    GPIO.output(dac, 0)