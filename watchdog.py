import pprint

import tweepy
import simpleaudio as sa
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, json

from config import *

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

wave_obj = sa.WaveObject.from_wave_file("itshighnoon.wav")

# userid of @PlayOverwatch: 2420931980
userid = 2420931980


def gottweet(tweet):
    wave_obj.play()


class MyListener(StreamListener):
    def on_data(self, tweet):
        tweet = json.loads(tweet)
        if tweet['user']['id'] == userid:
            print("Official Tweet: " + str(tweet))
            gottweet(tweet)
        else:
            print("Other: " + str(tweet))
        return True


def on_error(self, status):
    print("Error: " + str(status))
    return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(follow=[str(userid)])
