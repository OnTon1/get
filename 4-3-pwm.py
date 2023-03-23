import RPi.GPIO as gpio
import sys
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
dac = [24, 2]
gpio.setup(dac, gpio.OUT)
p = gpio.PWM(2, 50)
p2 = gpio.PWM(24, 50)
p.start(0)
p2.start(0)

try:
    while(1):
        DutyCycle = int(input())
        p.ChangeDutyCycle(DutyCycle)
        p2.ChangeDutyCycle(DutyCycle)
        print("{:.2f}".format(DutyCycle*3.3/100))
finally:
    gpio.output(2, 0)
    gpio.output(dac, 0)
    gpio.cleanup()