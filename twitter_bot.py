#!/usr/bin/env python

# A basic Python Raspberry Pi project with twitter API integration and GPIO usage
# it requires that you have a Pi camera installed and enabled

# Written by Mike Haldas
# Detailed documentation and wiring instruction here: http://www.cctvcamerapros.com/Pi-Alarm-MMS
# Email me at mike@cctvcamerapros.net if you have questions
# You can also reach me @haldas on twitter or +Mike Haldas on Google+
# If you make any improvements to this code or use it in a cool way, please let me know

import time
import subprocess
from twython import Twython

from gpio_pin_setup import *

IMG_WIDTH = "1280"
IMG_HEIGHT = "720"
IMG_NAME = "tweet-pic.jpg"
ROTATE = "180"

# your twitter app keys goes here
from secrets import *

# this is the command to capture the image using pi camera
snapCommand = "raspistill -rot " + ROTATE +  " -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT + " -o " + IMG_NAME

start_leds()

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print("System Ready - push button to take picture and tweet.\n")
led_ready()

try:
    while True:
        GPIO.wait_for_edge(BUTTON, GPIO.RISING)
        
        print("Program running...\n")
        for num in [3,2,1]:
            print(num)
            led_black()
            time.sleep(1)
            led_count_down()
            time.sleep(1)
        
        print("Capturing photo...\n")
        led_taking_photo()
        ret = subprocess.call(snapCommand, shell=True)
        photo = open(IMG_NAME, 'rb')
        
        print("Uploading photo to twitter...\n")
        led_tweeting()
        media_status = api.upload_media(media=photo)
        
        time_now = time.strftime("%H:%M:%S") # get current time
        date_now =  time.strftime("%d/%m/%Y") # get current date
        tweet_txt = "Photo captured by @DoorRobot"
        
        print("Posting tweet with picture...\n")
        led_processing()
        api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)
        
        #deprecated method replaced by upload_media() and update_status()
        #api.update_status_with_media(media=photo, status=tweetStr)
        
        print("Done - System ready again.\n")
        led_ready()

except KeyboardInterrupt:
    led_black()
    GPIO.cleanup()

finally:
    stop_leds()
    GPIO.cleanup() # ensures a clean exit
