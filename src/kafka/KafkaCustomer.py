from kafka import KafkaConsumer


def receive():
    consumer = KafkaConsumer('testTopic', group_id="py-test-group",
                             bootstrap_servers=['172.20.66.238:9092'])
    for message in consumer:
        print("receive = " + message.value)


if __name__ == '__main__':
    receive()
