import RPi.GPIO as GPIO

#setup GPIO using Broadcom SOC channel numbering
GPIO.setmode(GPIO.BCM)
BUTTON = 12 
GREEN = SYSTEM_READY      = 26 # indicates that program is ready to be run - GREEN
RED   = SYSTEM_RUNNING    = 13 # indicates that program is running - RED
BLUE  = SYSTEM_PROCESSING = 16 # indicates something

GPIO.setup(RED, GPIO.OUT) 
GPIO.setup(GREEN, GPIO.OUT) 
GPIO.setup(BLUE, GPIO.OUT) 
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GREEN_LED = GPIO.PWM(GREEN, 60)
RED_LED   = GPIO.PWM(RED, 60)
BLUE_LED  = GPIO.PWM(BLUE, 60)

def start_leds():
    RED_LED.start(0)
    BLUE_LED.start(0)
    GREEN_LED.start(0)

def stop_leds():
    RED_LED.stop()
    GREEN_LED.stop()
    BLUE_LED.stop()

def color_led(r, g, b):
    RED_LED.ChangeDutyCycle(r)
    GREEN_LED.ChangeDutyCycle(g)
    BLUE_LED.ChangeDutyCycle(b)

def led_ready():
    color_led(0, 100, 0)

def led_count_down():
    color_led(100,100,0)

def led_taking_photo():
    color_led(100,0,0)

def led_processing():
    color_led(0,100,100)

def led_tweeting():
    color_led(0,0,100)

def led_black():
    color_led(0,0,0)
