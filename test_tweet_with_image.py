import subprocess
from twython import Twython

from secrets import *

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

IMAGE_NAME = 'test.png'

ret = subprocess.call("raspistill -rot 180 -w 1280 -h 720 -o " + IMAGE_NAME, shell=True)
photo = open(IMAGE_NAME, 'rb')

print("Uploading image to twitter...\n")
media_status = api.upload_media(media=photo)

print("Posting tweet...\n")
api.update_status(media_ids=[media_status['media_id']], status="Second steps")

print("Done")
