# Write your code here :-)
from microbit import display, Image, button_a, button_b
import buildingbit
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        buildingbit.car_back(100, 100, 0)
    elif button_b.was_pressed():
        buildingbit.car_run(100, 100, 0)
    elif button_a.is_pressed() and button_b.is_pressed():
        buildingbit.car_stop()
