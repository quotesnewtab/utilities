#!/usr/bin/python
# coding=utf-8

from twython import Twython
import requests

# Get quote from Quotes New Tab API
quote = requests.get('https://api.quotesnewtab.com/v1/quotes/random').json()

# Twitter API credentials
API_KEY = ''
API_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Connect to twitter
twitter = Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Format tweet
tweet = '"%s" – %s' %(quote['quote'], quote['author'])

# Post tweet
twitter.update_status(status=tweet)
