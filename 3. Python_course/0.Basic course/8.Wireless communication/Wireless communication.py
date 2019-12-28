# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, button_a
import radio

display.show(Image.HEART)
radio.on()
radio.config(group=1)
a = 0

while True:
    if button_a.was_pressed():
        radio.send('flash')
    incoming = radio.receive()
    if incoming == 'flash':
        a = a + 1
        display.show(a)