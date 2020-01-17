# -*- coding: utf-8 -*-
import time
from functools import singledispatch

from kafka import KafkaProducer


@singledispatch
def send():
    # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
    producer = KafkaProducer(bootstrap_servers=["172.20.66.238:9092"])
    producer.send('testTopic', str(time.localtime(time.time())).encode('utf-8'))
    producer.close()


@send.register(str)
def _(topic, message, kafka_addr):
    # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
    producer = KafkaProducer(bootstrap_servers=kafka_addr)
    producer.send(topic, message.encode('utf-8'))
    producer.close()


if __name__ == '__main__':
    # topic = "testTopic-batch"
    topic = "testTopic-roll"
    message = """{"date":"%s"}"""
    kafka_addr = ["localhost:9092"]

    for i in range(1):
        timeStamp = time.time()
        localTime = time.localtime(timeStamp)
        strftime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        print(message % strftime)
        send(topic, message % strftime, kafka_addr)
        time.sleep(0.001)
