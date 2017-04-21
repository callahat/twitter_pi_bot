from twython import Twython

from secrets import *

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status='First steps')
