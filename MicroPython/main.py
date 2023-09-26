"""
Created by: Jack
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


# variable for microbit temperature
microbit_temperature = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        microbit_temperature = temperature()
        microbit_temperature = microbit_temperature + 273.15
        display.scroll(str("The temperature is:"))
        display.scroll(str(microbit_temperature) + ("K ."))
