#!/usr/bin/env python

# A basic Python Raspberry Pi project with twitter API integration and GPIO usage
# it requires that you have a Pi camera installed and enabled

# Written by Mike Haldas
# Detailed documentation and wiring instruction here: http://www.cctvcamerapros.com/Pi-Alarm-MMS
# Email me at mike@cctvcamerapros.net if you have questions
# You can also reach me @haldas on twitter or +Mike Haldas on Google+
# If you make any improvements to this code or use it in a cool way, please let me know

import os
import shutil
import time
import subprocess
import signal
from twython import Twython

from gpio_pin_setup import *

# your twitter app keys goes here
from secrets import *

from imageViaRaspistill import *
#from imageViaPicam import *

def handler(signum, frame):
    print(1)
    raise(Exception('Upload took too much time; Twitter unreachable?'))

# Three signal for signaling
signal.signal(signal.SIGALRM, handler)

start_leds()

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print("System Ready - push button to take picture and tweet.\n")
led_ready()

working_path = os.path.dirname(os.path.abspath(__file__))
print("working path:")
print(working_path)

uploaded_folder = working_path + '/images/uploaded/'
print("uploaded folder:")
print(uploaded_folder)

if not os.path.exists(uploaded_folder):
    os.makedirs(uploaded_folder)

try:
    while True:
        GPIO.wait_for_edge(BUTTON, GPIO.RISING)
        
        capture_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        image_folder = working_path + '/images/fresh/{:s}'.format(capture_time)
        
        print("Making image folder")
        os.makedirs(image_folder)
        
        print("Program running...\n")
        for num in [3,2,1]:
            print(num)
            led_black()
            time.sleep(1)
            led_count_down()
            time.sleep(1)
        
        led_black()
        time.sleep(1)
        
        print("Capturing photos...\n")
        for i in [1,2,3,4]:
            led_taking_photo()
            print("{:d} picture".format(i))
            captureImage(image_folder + "/{:d}.jpg".format(i))
            led_black()
            time.sleep(1)
        
        # If twitter is unavailable/network connection down, twython tries forever
        signal.alarm(10)
        
        try:
            print("Uploading photos to twitter...\n")
            led_tweeting()
            media_ids = []
            for i in [1,2,3,4]:
                photo = open(image_folder + "/{:d}.jpg".format(i), 'rb')
                media_status = api.upload_media(media=photo)
                media_ids.append(media_status['media_id'])
            
            tweet_txt = "Photos captured by @DoorRobot"
            
            print("Posting tweet with pictures...\n")
            led_processing()
            api.update_status(media_ids=media_ids, status=tweet_txt)
            
            print("Moving uploaded images to uploaded folder")
            shutil.move(image_folder, uploaded_folder + "/.")
        
        except:
            print("Took too long to send to twitter; netwrok or twitter down?")
            print(2)
        
        # Disable the alarm, past the potentially rough area
        signal.alarm(0)
        
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
