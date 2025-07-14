
## Twitter Sentiment Analysis — Spark Streaming, Kafka

**GitHub Repository:** [GitHub](#)

---

### 📌 Overview

A real-time data pipeline built using **Kafka**, **Spark Streaming**, and **Elasticsearch** to classify tweet sentiment and visualize trends through **Kibana dashboards**. Tweets related to geopolitical topics (`war`, `russia`, `ukraine`) are streamed, classified (`positive`, `negative`, `neutral`), and indexed for live analysis.

---

### 🔧 Tools & Technologies

* **Streaming & Messaging:** Apache Kafka
* **Processing:** Python, TextBlob, Spark Streaming
* **Data Ingestion:** Tweepy (Twitter API)
* **Search & Visualization:** Elasticsearch, Kibana
* **Other:** Logstash, JSON

---

### ⚙️ Key Features

* Streamed **real-time tweets** using Twitter API & Kafka producer
* Used **TextBlob** for lightweight sentiment analysis
* Indexed classified tweets into **Elasticsearch** for searchability
* Built a **Kibana dashboard** to monitor evolving sentiment trends
* Capable of processing **10K+ tweets/second** through Kafka pipeline

---

### 📈 Sample Output (Elasticsearch Document)

```json
{
  "message": "Unreal escalation happening right now in Kyiv.",
  "sentiment": "negative"
}
```

---

### 🧪 How to Run

#### 1. **Start Kafka**

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties  
bin/kafka-server-start.sh config/server.properties
```

#### 2. **Create Kafka Topic**

```bash
bin/kafka-topics.sh --create --topic tweets_ukr --bootstrap-server localhost:9092
```

#### 3. **Start Elasticsearch & Kibana**

```bash
./bin/elasticsearch  
./bin/kibana
```

#### 4. **Run Producer & Consumer**

```bash
python twitterProducer.py   # Streams tweets into Kafka
python kafkaConsumer.py     # Consumes from Kafka, classifies, and sends to Elasticsearch
```

---

### 🧠 Sentiment Classification Logic

* **Positive:** polarity > 0
* **Negative:** polarity < 0
* **Neutral:** polarity == 0

-

### 🔄 Potential Extensions

* Use **transformer models** (e.g., BERT, E5) for deeper sentiment classification
* Add **named entity tagging** or **topic clustering**
* Store long-term tweet data in **S3 or HDFS** for batch analysis

---

Note: This project was originally created during academic coursework using public datasets and entirely self-written code. It is shared solely for skill demonstration and not intended for academic reuse.
