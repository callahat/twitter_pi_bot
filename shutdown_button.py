import os
from gpio_pin_setup import *

GPIO.wait_for_edge(SHUTDOWN, GPIO.RISING)

print("Detected shutdown button press, shutting down")
os.system("sudo shutdown -h now")
