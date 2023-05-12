import json
import socket
import time

import kafka
import tweepy
from kafka import KafkaProducer
from transformers import pipeline
from tweepy import OAuthHandler, Stream

consumer_key="2n4nJi0ceJyTCpUXWVfaNrm9e"
consumer_secret_key="C14AZR2ywm8IGo6AG3HFVv1HpBVDROPOIixpJEFUUpQrrrIHSF"
access_token="1591993996372578305-OqY5MUm1PtyvfkZNAqxT7PDEgB5pwh"
access_token_secret="2u4UAstWkCGdh0NJDkZIAHDnnXtCW4tquVlXDL1DJ5MoP"
bearer_token="AAAAAAAAAAAAAAAAAAAAAHJHjQEAAAAAVw2IfdzQlrX7PUzbmRsofnPXyyc%3D5agRGG1ou6adpyCqRlpkOCYNSe77iTdRowoXYBF7WpAk5jwp4H"

client = tweepy.Client(bearer_token, consumer_key, consumer_secret_key, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)


search_terms = ["war", "russia", "ukraine"]


class TweetsStreams(tweepy.StreamingClient):
       
    def on_tweet(self,tweet):
        producer.send("tweets_ukr",tweet.text.encode('utf-8'))
        print(tweet.text)
        time.sleep(0.5)
        return True

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    #classifier = pipeline('sentiment-analysis')
    stream = TweetsStreams(bearer_token=bearer_token)

    for term in search_terms:
        stream.add_rules(tweepy.StreamRule(term))

    stream.filter(tweet_fields=["referenced_tweets"])