# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, button_a, button_b, sleep
import buildingbit

servoID = 1

display.show(Image.HEART)
buildingbit.servo(servoID, 90)
a = 90

while True:
    if button_a.is_pressed():
        a = a + 1
        sleep(1)
        if a > 180:
            a = 180
        buildingbit.servo(servoID, a)
    elif button_b.is_pressed():
        a = a - 1
        sleep(1)
        if a < 0:
            a = 0
        buildingbit.servo(servoID, a)


