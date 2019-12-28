# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import uart, display

uart.init(115200)
a = 0
display.show(0)
buf = ""

while True:
    if uart.any():
        buf = uart.read()
        uart.write(buf)
        a = a + 1
        if a > 9:
            display.show("A")
        else:
            display.show(a)