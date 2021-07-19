# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, pin8, sleep
import buildingbit
import music

display.off()
buildingbit.init_IR(pin8)
music.pitch(226)
sleep(300)
music.stop()


while True:
    #print(hex(buildingbit.get_IR(pin8)))

    value = buildingbit.get_IR(pin8)
    value = value >> 8
    #print(hex(value))

    # off
    if value == 0x00:
        music.play('c')
        sleep(1000)
        music.stop()
    # up
    elif value == 0x80:
        music.play('c')
        sleep(1000)
        music.stop()
    # light
    elif value == 0x40:
        music.play('c')
        sleep(1000)
        music.stop()
    # left
    elif value == 0x20:
        music.play('c')
        sleep(1000)
        music.stop()
    # buzzer
    elif value == 0xa0:
        music.play('c')
        sleep(1000)
        music.stop()
    # right
    elif value == 0x60:
        music.play('c')
        sleep(1000)
        music.stop()
    # spinleft
    elif value == 0x10:
        music.play('c')
        sleep(1000)
        music.stop()
    # down
    elif value == 0x90:
        music.play('c')
        sleep(1000)
        music.stop()
    # spinright
    elif value == 0x50:
        music.play('c')
        sleep(1000)
        music.stop()
    # +
    elif value == 0x30:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 0
    elif value == 0xb0:
        music.play('c')
        sleep(1000)
        music.stop()
    # -
    elif value == 0x70:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 1
    elif value == 0x08:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 2
    elif value == 0x88:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 3
    elif value == 0x48:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 4
    elif value == 0x28:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 5
    elif value == 0xa8:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 6
    elif value == 0x68:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 7
    elif value == 0x18:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 8
    elif value == 0x98:
        music.play('c')
        sleep(1000)
        music.stop()
    # number 9
    elif value == 0x58:
        music.play('c')
        sleep(1000)
        music.stop()
    # long pressed
    elif value == 0xff:
        music.pitch(500)
        music.play('c')
        sleep(1000)
        music.stop()
