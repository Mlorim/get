import RPi.GPIO as GPIO
import time

def to_bin(i):
    return [int(j) for j in bin(i)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]



comp = 14
troyka = 13
max_V = 3.3
bits = len(dac)
levels = 2 ** bits
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def adc(value):
    out = to_bin(value)
    GPIO.output(dac, out)
    return out



try:
    while True:
        for value in range(256):
            out = adc(value)
            time.sleep(0.01)
            voltage = (value / levels) * max_V
            comp_val = GPIO.input(comp)
            if comp_val == 1:
                print('ADC value ', value, '=>', out, 'voltage', voltage)
                break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()