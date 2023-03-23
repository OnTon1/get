import RPi.GPIO as gpio
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while(1):
        T = input('Please enter a number\n')
        t = int(T)/(256*2)
        for i in range(256):
            gpio.output(dac, dec2bin(i))
            print(i/256*3.3)
            sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, dec2bin(i))
            print(i/256*3.3)
            sleep(t)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()