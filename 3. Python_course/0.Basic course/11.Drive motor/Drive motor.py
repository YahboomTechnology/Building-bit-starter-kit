# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import buildingbit

display.show(Image.HAPPY)
buildingbit.car_run(255, 255, 1000)
buildingbit.car_stop()
sleep(1000)
buildingbit.car_back(255, 255, 1000)
buildingbit.car_stop()
