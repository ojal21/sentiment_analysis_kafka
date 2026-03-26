FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install tweepy kafka-python

CMD ["python", "twitterReader.py"]