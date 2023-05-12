from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json
from textblob import TextBlob
import re 
#elasticSearch = Elasticsearch(hosts=['localhost'], port= '9200',scheme='https')
elasticSearch = Elasticsearch("http://localhost:9200")

if __name__ == "__main__":
   
    search_terms = ["war", "russia", "ukraine"]
    
    consumer=KafkaConsumer("tweets_ukr", auto_offset_reset='latest')
    
    for line in consumer:
        print(line)
       # dict_data = json.loads(line.value)
        sentence=str(line.value)
        tweet = TextBlob(sentence)
        sentiment = tweet.sentiment.polarity
        tweet_sentiment = ""
        print("sentiment", sentiment)    
        if sentiment>0: tweet_sentiment='positive'
        elif sentiment<0: tweet_sentiment='negative'
        elif sentiment==0: tweet_sentiment='neutral'
        
        elasticSearch.index(
            index="tweets_ukr",
            document={
                "message":sentence,
                "sentiment":tweet_sentiment
            }
            
        )
        