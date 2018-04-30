import os
import shutil
import signal
from twython import Twython

# your twitter app keys goes here
from secrets import *

def handler(signum, frame):
    print(1)
    raise(Exception('Upload took too much time; Twitter unreachable?'))

# Three signal for signaling
signal.signal(signal.SIGALRM, handler)

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print("Running uploader...")
working_path = os.path.dirname(os.path.abspath(__file__))
print("working path:")
print(working_path)

uploaded_folder = working_path + '/images/uploaded/'
print("uploaded folder:")
print(uploaded_folder)

fresh_image_folder = os.path.join(working_path, 'images/fresh/')
print("fresh images folder:")
print(fresh_image_folder)

fresh_image_sets = os.listdir(fresh_image_folder)

# If twitter is unavailable/network connection down, twython tries forever
signal.alarm(10)

try:
    for fresh_image_set in fresh_image_sets:
        image_folder = os.path.join(fresh_image_folder, fresh_image_set)
        print("Attempting to upload:")
        print(image_folder)
        
        print("Uploading photos to twitter...\n")
        media_ids = []
        for i in [1,2,3,4]:
            photo = open(image_folder + "/{:d}.jpg".format(i), 'rb')
            media_status = api.upload_media(media=photo)
            media_ids.append(media_status['media_id'])
        
        tweet_txt = "Photos captured by @DoorRobot around " + fresh_image_set
        
        print("Posting tweet with pictures...\n")
        api.update_status(media_ids=media_ids, status=tweet_txt)
        
        print("Moving uploaded images to uploaded folder")
        shutil.move(image_folder, uploaded_folder + "/.")

except:
    print("Took too long to send to twitter; network or twitter down?")
    print(2)

# Disable the alarm, past the potentially rough area
signal.alarm(0)

