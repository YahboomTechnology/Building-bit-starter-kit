# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import buildingbit

display.show(Image.HAPPY)


while True:
    a = buildingbit.ultrasonic()
    print(a)
