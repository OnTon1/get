import RPi.GPIO as gpio
import sys

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def check(a):
    if a.isdigit() and int(a)==float(a) and 0<=int(a)<=255:
        return 1
    else:
        return 0

try:
    while(1):
        a = input('input value 0-255\n')
        if a == 'q':
            sys.exit()
        elif check(a) == 1:
            gpio.output(dac, dec2bin(int(a)))
            print(int(a)/256*3.3)
        else:
            print('Error. Input number 0-255\n')
finally:
    gpio.output(dac, 0)
    gpio.cleanup()