import RPi.GPIO as GPIO


dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
v = 3.3

def to_bin(i):
    return [int(j) for j in bin(i)[2:].zfill(8)]


try:
    while True:
        n = input('enter n => int and 0 <= int(n) <= 255: ')
        if n == 'q':
            print('Quit')
            break
        else:
            if n.isdigit():

                if '.' in n or not(0 <= int(n) <= 255):
                    print('incorrect input (n => int and 0 <= int(n) <= 255)')

                else:
                    n = int(n)
                    GPIO.output(dac, to_bin(n))
                    print('U = ', round(v*n/(2**len(dac)), 3), ' V')    

            else:
                print('incorrect input (n => int)')

finally:
    GPIO.output(dac, 0)