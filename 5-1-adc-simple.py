import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        gpio.output(dac, dec2bin(i))
        sleep(0.0007)
        cmpvalue = gpio.input(comp)
        if cmpvalue == 0:
            return i

try:
    while True:
        print('V = {:.2f}'.format(3.3*adc()/256))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()