import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial = 1)

comp = 4
troyka = 17
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def adc():
    weight = 0
    for i in range(7, -1, -1):
        weight = weight + 2**i
        gpio.output(dac, dec2bin(weight))
        time.sleep(0.001)
        if gpio.input(comp) == 0:
            weight = weight - 2**i
    return weight

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    voltage = 0
    result_arr = []
    time_start = time.time()
    N = 0

    print('Зарядка конденсатора')
    while voltage < 256*0.90:
        voltage = adc()
        result_arr.append(voltage)
        N = N + 1
        gpio.output(leds, dec2bin(voltage))
    
    gpio.setup(troyka, gpio.OUT, initial = 0)

    print('Разрядка конденсатора')
    while voltage > 256*0.1:
        voltage = adc()
        result_arr.append(voltage)
        N = N + 1
        gpio.output(leds, dec2bin(voltage))

    time_measurement = time.time() - time_start
    result_arr_str = [str(i) for i in result_arr]

    print('Запись данных')
    with open('data.txt', 'w') as f:
        for i in result_arr:
            f.write("\n".join(result_arr_str))
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_measurement/N))
        f.write(str(3.3/256))

    print('Графики')
    y = [i/256*3.3 for i in result_arr]
    x = [i*time_measurement/N for i in range(len(result_arr))]
    pyplot.plot(x, y)
    pyplot.xlabel('Время, t')
    pyplot.ylabel('Напряжение, V')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
