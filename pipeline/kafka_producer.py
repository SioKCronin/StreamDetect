import sys
import boto3
import botocore

from datetime import datetime
from kafka.producer import KafkaProducer
from time import sleep

BUCKET_NAME = 'wikipedia-raw-xml-data'
DOCS = 'mvp_docs.json'
QUERIES = 'mvp_queries.json'
ip_addr = '34.212.143.68' 

class Producer(object):

    def __init__(self, addr):
        self.producer = KafkaProducer(bootstrap_servers=addr)

    def read_from_s3(self):
        s3 = boto3.client('s3') #low-level functional API
        my_bucket = resource.Bucket(BUCKET_NAME)

        for datum in docs:
            self.producer.send('docs', datum)

if __name__=='__main__':
    prod = Producer(ip_addr)
    prod.read_from_s3(DOCS)
    prod.read_from_s3(QUERIES)
