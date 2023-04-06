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
    weight = 0
    for i in range(7, -1, -1):
        weight = weight + 2**i
        gpio.output(dac, dec2bin(weight))
        sleep(0.001)
        if gpio.input(comp) == 0:
            weight = weight - 2**i
    return weight
try:
    while True:
        print('V = {:.2f}'.format(3.3*adc()/256))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()