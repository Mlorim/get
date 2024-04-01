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
    for i in range(7, -1, -1):
        out = to_bin(value)
        GPIO.output(dac, out)
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            value -= 2**(i)
            value += 2**(i-1)
        else:
            value += 2**(i-1)
    
    return out, value



try:
    while True:
        out, value = adc(128)
        voltage = (value / levels) * max_V
        print('ADC value ', value, '=>', out, 'voltage', voltage)  

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()