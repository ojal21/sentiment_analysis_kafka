import json
import socket
import time

import kafka
import tweepy
from kafka import KafkaProducer
from transformers import pipeline
from tweepy import OAuthHandler, Stream
import os

api_key = os.getenv("TWITTER_API_KEY")


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