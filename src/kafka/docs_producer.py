import argparse
import boto3
from kafka import SimpleProducer, KafkaClient
from time import sleep

if __name__=='__main__':

    host = '52.11.70.247' 
    port = 9092

    # arg parsing
    parser = argparse.ArgumentParser(description="Feed Kafka data from file")
    parser.add_argument("file", help="S3 filename")
    parser.add_argument("topic", help="Kafka topic to feed")
    parser.add_argument("-host", default='52.11.70.247', help="Public IP address of a Kafka node")
    parser.add_argument("-port", default=9092, help="port for zookeeper, default 9092")
    args = parser.parse_args()

    # get a client
    #print("Connecting to Kafka note {0}:{1}".format(args.host, args.port))
    kafka = KafkaClient("{0}:{1}".format(host, port))
    producer = SimpleProducer(kafka)

    # read data from S3
    client = boto3.client('s3') #low-level functional API
    resource = boto3.resource('s3') #high-level object-oriented API
    my_bucket = resource.Bucket('wikipedia-raw-xml-data')
    f = my_bucket.lookup(args.file)

    # send messages to Kafka
    for datum in f:
        producer.send_messages(args.topic, datum)
