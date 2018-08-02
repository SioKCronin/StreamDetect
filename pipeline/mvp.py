import sys
import boto3
import botocore
import json
import redis
import threading, logging, time
import multiprocessing
from datetime import datetime
from kafka.producer import KafkaProducer
from time import sleep

from kafka import KafkaConsumer
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

kafka_ip = '34.212.143.68'

BUCKET_NAME = 'wikipedia-raw-xml-data'
DOCS = 'MOCK_DATA.json'
QUERIES = 'mvp_queries.json'
ip_addr = '34.212.143.68' 
query = "test"

# Create topic






class Producer(threading.Thread):

    #def __init__(self, addr):
    #    self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    #def read_from_s3(self):

    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers='DNS from master:9092')

        for i in x:
            producer.send('my_topic', b'i')
            producer.flush()
            time.sleep(0.5)

        while not self.stop_event.is_set():
            s3 = boto3.client('s3') #low-level functional API
            my_bucket = resource.Bucket(BUCKET_NAME)

            for datum in docs:
                self.producer.send('docs', datum)

            time.sleep(1)

        producer.close()

class Consumer(multiprocessing.Process):

    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer('my_topic', bootstrap_servers='DNS master node:9092')

        for msg in consumer:
            print(msg)

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()

def main():
    tasks = [Producer(),Consumer()]

    for t in tasks:
        t.start()

    time.sleep(10)

    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()

#    if len(sys.argv) != 3: 
#        print("Usage: kakfa_producer.py", file=sys.stderr)
#        sys.exit(-1)
#
#    # Register the spark context
#    sc = SparkContext(appName="StreamingSearch")
#    ssc = StreamingContext(sc, 5)
#
#    zoo, topic = sys.argv[1:]
#    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
#    lines = kvs.map(lambda x: x[1])
#    counts = lines.flatMap(lambda line: line.split(" ")) \
#        .map(lambda word: (word, 1)) \
#        .reduceByKey(lambda a, b: a+b)
#    counts.pprint()
#
#    # Get data stream from kafka topic
#    #docs = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])
#    #queries = KafkaConsumer('docs',group_id='stream', bootstrap_servers=[kafka_ip])
#
#    ssc.start()
#    ssc.awaitTermination()
#
#if __name__=='__main__':
#    prod = Producer(ip_addr)
#    prod.read_from_s3(DOCS)
#    prod.read_from_s3(QUERIES)
