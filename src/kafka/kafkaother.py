
from pykafka import KafkaClient

def read_topic():
    """
    得到所有主题
    """
    client = KafkaClient(hosts="172.20.66.238:9092")
    for topic in client.topics:
        print(topic)
if __name__ == '__main__':
    read_topic()