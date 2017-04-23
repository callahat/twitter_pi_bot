import time
from gpio_pin_setup import *

start_leds()
try:
    while 1:
        for dc in range(0, 101, 5):
            RED_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(0, 101, 5):
            GREEN_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(0, 101, 5):
            BLUE_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            BLUE_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            RED_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            GREEN_LED.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
stop_leds()
GPIO.cleanup()
