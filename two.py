# two.py
import tweepy
from textblob import TextBlob
#from tweepy.auth import OAuthHandler

consumer_key = 'B2v9FmKlMnU4aqYs2DDcPw2ps'
consumer_secret = 'Qpui0muwm5g0bmrdmcgrThIhuWk427IotdkWoVJ75immhsDD9j'

access_token = '963364072841449472-JZVKSql2ss5XmfJjxAULEefXq9TzbaY'
access_token_secret = 'yGsd2BaeWut2kSMI8YrFiHT3LkNu0ydWi8gW1MKF7y30c'

from tweepy.auth import OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print (api.verify_credentials())

enterprise =input('Intro the enterprise name here ')
public_tweets = api.search(str(enterprise))

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	pass