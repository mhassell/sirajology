import tweepy
from textblob import TextBlob

consumer_key = '7qCofTZpBDA2wnykbVToe4vrA'
consumer_secret = raw_input('Input API secret key: ')

access_token = '3893402631-eyHfTGjhJm4dbU8kr3RTAIV6xViSVWaLTKjyZDz'
access_token_secret = raw_input('Input Access Token Secret: ')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
