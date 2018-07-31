import os
import json

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from datetime import datetime

# Obtain kafka brokers from config
k_docs_topic: "docs"
k_docs_broker: LOCATION
k_query_topic: "docs"
k_query_broker: LOCATION

# Register the spark context
conf = SparkConf().setAppName("stream")
sc = SparkContext(conf=conf)

# Register the streaming context
ssc = StreamingContext(sc, 5)
ssc.checkpoint("hdfs://ec2-35-167-24-116.us-west-2.compute.amazonaws.com:9000/checkpoint/")

# Get data stream from kafka topic
kafkaStream = KafkaUtils.createDirectStream(ssc, [k_docs_topic], {"boostrap.servers": k_docs_broker})

# Load each event into stream
lines = kafkaStream.map(lambda (key, value): json.loads(value))

# Lines of output - the Lucene-Luwak piece

ssc.start()
ssc.awaitTermination()
