  	#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy
from flask import Flask, render_template

consumer_key = "5CkIgQP63J0spFWSIlR0oJSGZ"
consumer_secret = "H51DyzetfMcSbqFkY6wfSgfp6tvaqkMF6PhKWrxn4TdQ9kRmyH"
access_key = "323720413-2FwITRACbcH7bONW5RKdaCwdkuWq6zaCJjkeYiNX"
access_secret = "tY70UXffjIaEDr8teSGYC8qBKw6ErffgOkPchkLVBlEG5"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/hello")
def index():
	

	public_tweets = api.home_timeline(count=100)
	return str(public_tweets)	

@app.route("/")
def hello():
    #Get your Twitter API credentials and enter them here
	consumer_key = "5CkIgQP63J0spFWSIlR0oJSGZ"
	consumer_secret = "H51DyzetfMcSbqFkY6wfSgfp6tvaqkMF6PhKWrxn4TdQ9kRmyH"
	access_key = "323720413-2FwITRACbcH7bONW5RKdaCwdkuWq6zaCJjkeYiNX"
	access_secret = "tY70UXffjIaEDr8teSGYC8qBKw6ErffgOkPchkLVBlEG5"


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True)

	public_tweets = api.home_timeline(count=100)
	return render_template('index.html')

if __name__ == "__main__":
  	app.run('localhost', 3000)


