from picamera import PiCamera
import tweepy
import json
from random import choice




camera = PiCamera()
camera.capture('/home/pi/Whoopie/fart.jpg')
camera.close()

tweets = ['Oops i just sat on a Whoopie Cushion', 'I think it smells funny around here', 'Did someone just fart?']

my_tweet = choice(tweets)


with open('/home/pi/Whoopie/twitter_auth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)

twitter.update_with_media('/home/pi/Whoopie/fart.jpg', my_tweet)