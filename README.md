# Twitter Sentiment Analysis using Spark Streaming and Kafka

• Used Spark Streaming and Kafka to stream Twitter data in real-time
• Performed sentiment analysis on relevant tweets. Visualized results using ElasticSearch and Kibana

**Consumer**

Kafka consumer, takes tweets in and passes it forward to conduct sentiment analysis.
Uses new TwitterAPI to read tweets.

**Reader**

Takes input from consumer and performs sentiment analysis. Gives each tweet a tag - positive, neutral, negative.  The output is then displayed on elastic dashboard.

