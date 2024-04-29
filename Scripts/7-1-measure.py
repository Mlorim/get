import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def to_bin(i):
    return [int(j) for j in bin(i)[2:].zfill(8)]


def adc(value):
    for i in range(7, 0, -1):
        out = to_bin(value)
        GPIO.output(dac, out)
        time.sleep(0.005)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            value -= 2**(i)
            value += 2**(i-1)
        else:
            value += 2**(i-1)
    voltage = (value / levels) * max_V
    return value           
    

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]

comp = 14
troyka = 13
max_V = 3.3
bits = len(dac)
levels = 2 ** bits
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    data = []
    start = time.time()
    GPIO.output(troyka, GPIO.HIGH)
    volt = 0
    while volt <= 190:
        volt = adc(128)
        data.append(volt)
    GPIO.output(troyka, 0)
    end_charge = time.time()
    while volt > 167:
        volt = adc(128)
        data.append(volt)
        
    end = time.time()
    duration = end - start
    duration_charge = end_charge - start
    plt.plot(data)
    freq = 1/duration_charge
    step = 3.3/2**bits
    f = open("data.txt", "w")
    for res in data:
        f.write(str(round(res, 3))+'\n')
    f.close()
    f = open("settings.txt", "w")
    f.write('charging frequence = ' + str(freq) + '\n')
    f.write('step = ' + str(step))
    f.close()
    print('charging - ', duration_charge)
    print('to 2.14 V - ', duration)
    print('charging frequence = ', freq/len(data))
    print('step = ', step)

    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

