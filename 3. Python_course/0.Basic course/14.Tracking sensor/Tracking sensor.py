# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import buildingbit

display.show(Image.NO)


while True:
    trakeL = buildingbit.traking_sensor_L()
    trakeR = buildingbit.traking_sensor_R()
    if trakeL and trakeR:
        display.show(Image.HAPPY)
    elif trakeL is True:
        display.show("L")
    elif trakeR is True:
        display.show("R")
    else:
        display.show(Image.NO)
