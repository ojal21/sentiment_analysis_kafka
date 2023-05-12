# Steps to Run


1. Start Zookeeper: 
         bin/zookeeper-server-start.sh config/zookeeper.properties
2. Start Kafka
        bin/kafka-server-start.sh config/server.properties
3. Create Topics: 
        bin/kafka-topics.sh --create --topic tweets_ukr--bootstrap-server localhost:9092
4. Start consumer:
	bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic tweets_ukr --from-beginning
        


ELK Stack : 
1. Elasticsearch (At the directory of Elasticsearch) :
    ./bin/elasticsearch
2. Kibana (At the directory of Kibana) :
    ./bin/kibana
3. Logstash (At the directory of Logstash) :
    ./bin/logstash  (OR) ./bin/logstash -f /path/to/conf/logstash.conf
    

This Application is built on Tweepy - Python for Twitter API Analysis.
1. Run the python file using command : 
        python twitterReader.py
2. . Run the python file using command : 
        python kafkaConsumer.py


1. Logstash requires its .conf file to point the input and output. 
ex. 
input {


  kafka {
      bootstrap_servers => ["localhost:9092"]
      topics => ["tweets_ukr"]
  }

}

output {
  elasticsearch { 
    hosts => ["localhost:9200"]
    index => "tweets_ukr"
   }
  stdout { codec => rubydebug }
}
