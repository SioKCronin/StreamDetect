import sys
import os
import json
import redis
from datetime import datetime
from kafka import KafkaConsumer

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

kafka_ip = '34.212.143.68'

def Streamer(self):

    # Register the spark context
    conf = SparkConf().setAppName("stream")
    sc = SparkContext(appName="StreamingSearch")
    ssc = StreamingContext(sc, 5)

    # Get data stream from kafka topic
    docs = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])
    queries = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])
    #docs = KafkaUtils.createDirectStream(ssc, zkeeper_id, ["docs"], {"bootstrap.servers": kafka_broker_ip})
    #queries = KafkaUtils.createDirectStream(ssc, ["queries"], {"boostrap.servers": kafka_broker_ip})

    return docs

    #for message in docs:
    #    print(message)

    # Lucene tokenizing
    # Lucene query indexing
    # Publish matches to Redis

    #ssc.start()
    #ssc.awaitTermination()

if __name__ == '__main__':
    print(Streamer(kafka_ip))

