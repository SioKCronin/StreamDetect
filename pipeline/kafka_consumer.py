import sys
import os
import json
import redis

from datetime import datetime
from kafka import KafkaConsumer

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":

    query = KafkaConsumer('query', bootstrap_servers='ec2-52-13-241-228.us-west-2.compute.amazonaws.com:9092')
    docs = KafkaConsumer('docs', bootstrap_servers='ec2-52-13-241-228.us-west-2.compute.amazonaws.com:9092')

    # Register the spark context
    #sc = SparkContext(appName="Sift")
    #ssc = StreamingContext(sc, 5)

    for msg in docs:
        print(msg)

    #zoo, topic = sys.argv[1:]
    #kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    #lines = kvs.map(lambda x: x[1])
    #counts = lines.flatMap(lambda line: line.split(" ")) \
    #    .map(lambda word: (word, 1)) \
    #    .reduceByKey(lambda a, b: a+b)
    #counts.pprint()

    ## Get data stream from kafka topic
    ##docs = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])
    ##queries = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])

    ssc.start()
    ssc.awaitTermination()
