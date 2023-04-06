import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
leds.reverse()
comp = 4
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
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

def func(a):
    a = int(a/256*10)
    arr = [0]*8
    for i in range(a - 1):
        arr[i] = 1
    return arr
try:
    while True:
        gpio.output(leds, func(adc()))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()

