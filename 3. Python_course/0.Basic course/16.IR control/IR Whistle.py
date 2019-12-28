# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, pin8, sleep
import buildingbit
import music

display.off()
buildingbit.init_IR(pin8)
buildingbit.car_run(100, 100, 0)
music.pitch(226)
sleep(300)
music.pitch(0)


while True:
    # print(hex(buildingbit.get_IR(pin8)))

    value = hex(buildingbit.get_IR(pin8))
    if value == "-0x1":
        buildingbit.car_run(0, 0, 0)
    elif value == "0xffff":
        buildingbit.car_run(0, 0, 0)
    else:
        value = value[0:4]
        if value == "0xff":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x80":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x40":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x20":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0xa0":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x60":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x10":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x90":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x50":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x30":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0xb0":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x70":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x8f":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x88":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x48":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x28":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0xa8":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x68":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x18":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x98":
            music.pitch(226)
            sleep(300)
            music.pitch(0)
        elif value == "0x58":
            music.pitch(226)
            sleep(300)
            music.pitch(0)

