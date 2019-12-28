# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import buildingbit
import radio

display.show(Image.HEART)
radio.on()
radio.config(group=1)


while True:
    incoming = radio.receive()
    if incoming == 'up':
        buildingbit.car_back(150, 0, 0)
    elif incoming == 'down':
        buildingbit.car_run(150, 0, 0)
    elif incoming == 'left':
        buildingbit.car_back(0, 30, 0)
    elif incoming == 'right':
        buildingbit.car_run(0, 30, 0)
    elif incoming == 'stop':
        buildingbit.car_stop()

    if incoming == 'R':
        buildingbit.car_HeadRGB(255, 0, 0)
    elif incoming == 'G':
        buildingbit.car_HeadRGB(0, 255, 0)
    elif incoming == 'B':
        buildingbit.car_HeadRGB(0, 0, 255)
    elif incoming == 'Y':
        buildingbit.car_HeadRGB(255, 255, 0)
    elif incoming == 'turn_off':
        buildingbit.car_HeadRGB(0, 0, 0)
