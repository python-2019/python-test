# -*- coding: utf-8 -*-
import json
import time

from kafka import KafkaProducer
from kafka import KafkaConsumer
from pykafka import KafkaClient


def send():
    # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
    producer = KafkaProducer(bootstrap_servers=["172.20.66.238:9092"])
    producer.send('testTopic', str(time.time()).encode('utf-8'))
    producer.close()




if __name__ == '__main__':
    send()