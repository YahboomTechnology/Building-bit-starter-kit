# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import buildingbit

display.show(Image.HAPPY)

while True:
    sensorL = buildingbit.traking_sensor_L()
    sensorR = buildingbit.traking_sensor_R()
    if sensorL is False and sensorR is False:
        buildingbit.car_run(100, 100, 0)
    elif sensorL is False and sensorR is True:
        buildingbit.car_spinright(100, 100, 0)
    elif sensorL is True and sensorR is False:
        buildingbit.car_spinleft(100, 100, 0)
    else:
        buildingbit.car_stop()
