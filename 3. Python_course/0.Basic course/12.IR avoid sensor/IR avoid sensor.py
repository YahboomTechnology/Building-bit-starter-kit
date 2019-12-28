# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display
import buildingbit
import music

display.off()
avoid = False


while True:
    avoid = buildingbit.avoid_sensor()
    if avoid is True:
        music.pitch(266)
    else:
        music.pitch(0)
