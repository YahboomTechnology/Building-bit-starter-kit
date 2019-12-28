# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display
import buildingbit

display.off()

while True:
    avoid = buildingbit.avoid_sensor()
    if avoid is True:
        buildingbit.car_back(100, 100, 1000)
        buildingbit.car_spinright(100, 100, 1000)
    else:
        buildingbit.car_run(100, 100, 0)
