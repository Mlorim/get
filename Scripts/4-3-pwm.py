import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# GPIO.setup(9, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

v = 3.3
FREQUENCY = 1000
DUTY_CYCLE = 0
# p = GPIO.PWM(9, FREQUENCY)
p = GPIO.PWM(21, FREQUENCY)
p.start(DUTY_CYCLE)

try:
    while True:
        DUTY_CYCLE = int(input())
        p.start(DUTY_CYCLE)
        print(v* DUTY_CYCLE/100)
finally:
    p.stop()
    GPIO.cleanup()
