import tweepy
from textblob import TextBlob

import numpy as np
import operator

#step 1 : get authentication
consumer_key = 'COMSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#step 2: prepare query features
list_of_hashTags = ['Startup','ArtificialIntelligence','MachineLearning','Entrepreneurship']

since_date = "2017-01-01"
until_date = "2017-06-05"

#step 3 - Function of labelisation of analysis
def get_label(analysis, threshold = 0.1):
	if analysis.sentiment.polarity>threshold:
		return 'Positive'
	elif analysis.sentiment.polarity>-0.1:
		return 'Neutral'
	else:
		return 'Negative'

#step 4: retrive tweets and save them
all_polarities = dict()
for hash_tag in list_of_hashTags:
	this_hashTag_tweets = api.search(hash_taggit)
	with open('%s_tweets.csv' % hash_tag,'w') as this_hashTag_file:
		this_hashTag_file.write('tweet, sentiment_label\n')
		for tweet in this_hashTag_tweets:
			analysis = TextBlob(tweet.text)
			inputt = tweet.text + ", " + get_label(analysis) + "\n"
			this_hashTag_file.write(inputt)
