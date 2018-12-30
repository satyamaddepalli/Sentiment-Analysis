import tweepy  
from textblob import TextBlob

Consumer_Key='DZi20CGVhaCeNZ1GqPjHGdHfw'
Consumer_Secretkey='smyjQtp7zm3PdRddDqhzkqaiQaj4vUOzMqy3qY7NcDoMhGPtpn'
Access_Key='352453956-dCOAqeLWgkTfhRbdKVp5qQXN8zfcnN1iQaNH6jSo'
Access_SecretKey='8g98IYfXjlm6A9vp6OtqE6AgkdxwpSZuY86SFVAJ6Gr2X'

oAuth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secretkey)
oAuth.set_access_token(Access_Key,Access_SecretKey)
api=tweepy.API(oAuth)

public_tweets=api.search('@realDonaldTrump')

for tweet in public_tweets:
    print(tweet.text)
    analsys=TextBlob(tweet.text)
    print(analsys.sentiment)
