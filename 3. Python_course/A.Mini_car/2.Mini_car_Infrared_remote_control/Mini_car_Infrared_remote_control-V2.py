# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# from microbit import *
from microbit import display, sleep, pin8, pin16
import buildingbit
import music
import neopixel

display.off()
np = neopixel.NeoPixel(pin16, 3)
np.clear()
buildingbit.init_IR(pin8)
buildingbit.car_run(0, 0, 0)

speed = 100
a = 0


while True:
    # print(hex(buildingbit.get_IR(pin8)))
    value = buildingbit.get_IR(pin8)
    value = value >> 8

    # default
    if value == -0x01:
        a = a + 1
        if (a > 3):
            buildingbit.car_stop()
            a = 0
    # long pressed
    elif value == 0xff:
        a = 0
    else:
        # off
        if value == 0x00:
            buildingbit.car_HeadRGB(0, 0, 0)
        # up
        elif value == 0x80:
            buildingbit.car_run(speed, speed, 0)
        # light
        elif value == 0x40:
            buildingbit.car_HeadRGB(255, 255, 255)
        # left
        elif value == 0x20:
            buildingbit.car_right(speed, 0)
        # buzzer
        elif value == 0xa0:
            music.pitch(698)
            sleep(400)
            music.stop()
        # right
        elif value == 0x60:
            buildingbit.car_left(speed, 0)
        # spinleft
        elif value == 0x10:
            buildingbit.car_spinright(speed, speed, 0)
        # down
        elif value == 0x90:
            buildingbit.car_back(speed, speed, 0)
        # spinright
        elif value == 0x50:
            buildingbit.car_spinleft(speed, speed, 0)
        # +
        elif value == 0x30:
            speed = speed + 40
            if speed > 255:
                speed = 255
                music.pitch(500)
                sleep(300)
                music.stop()
            else:
                music.pitch(226)
                sleep(300)
                music.stop()
        # number 0
        elif value == 0xb0:
            speed = 100
            music.pitch(226)
            sleep(300)
            music.stop()
        # -
        elif value == 0x70:
            speed = speed - 40
            if speed < 0:
                speed = 0
                music.pitch(60)
                sleep(300)
                music.stop()
            else:
                music.pitch(226)
                sleep(300)
                music.stop()
        # number 1
        elif value == 0x08:
            music.pitch(262)
            sleep(500)
            music.stop()
        # number 2
        elif value == 0x88:
            music.pitch(294)
            sleep(500)
            music.stop()
        # number 3
        elif value == 0x48:
            music.pitch(330)
            sleep(500)
            music.stop()
        # number 4
        elif value == 0x28:
            music.pitch(349)
            sleep(500)
            music.stop()
        # number 5
        elif value == 0xa8:
            music.pitch(392)
            sleep(500)
            music.stop()
        # number 6
        elif value == 0x68:
            music.pitch(440)
            sleep(500)
            music.stop()
        # number 7
        elif value == 0x18:
            music.pitch(494)
            sleep(500)
            music.stop()
        # number 8
        elif value == 0x98:
            np[0] = (255, 0, 0)
            np[1] = (0, 255, 0)
            np[2] = (0, 0, 255)
            np.show()
        # number 9
        elif value == 0x58:
            np.clear()
