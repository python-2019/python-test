import os
import platform
import sys

zk = "localhost:2181"
kafka_addr = "localhost:9092"


def sys_platform():
    if platform.system() == 'Windows':
        return 0
    if platform.system() == 'Linux':
        return 1

if __name__ == '__main__':
    sys_platform = sys_platform()
    if sys_platform == 0:
        action = sys.argv[1]
        if action == 'list':
            list_zk = "bin\windows\kafka-topics.bat --zookeeper %s --list" % zk
            print(list_zk)
            os.system(list_zk)

        elif action == 'create':
            topic = sys.argv[2]
            create_topic = "bin\windows\kafka-topics.bat --create --zookeeper %s --replication-factor 1 --partitions 1 --topic %s" % (kafka_addr, topic)
            print(create_topic)
            os.system(create_topic)

        elif action == 'send':
            topic = sys.argv[2]
            send_topic = "bin\windows\kafka-console-producer.bat --broker-list %s --topic %s" % (kafka_addr, topic)
            print(send_topic)
            os.system(send_topic)

        elif action == 're':
            topic = sys.argv[2]
            re_topic = "bin\windows\kafka-console-consumer.bat  --zookeeper %s  --topic %s --from-beginning" % (zk, topic)
            print(re_topic)
            os.system(re_topic)

    elif sys_platform == 1:
        action = sys.argv[1]
        if action == 'list':
            s_list_zk = "bin\kafka-topics.sh --zookeeper %s --list" % zk
            os.system(s_list_zk)

        elif action == 'create':
            topic = sys.argv[2]
            create_topic = "bin\kafka-topics.sh --create --zookeeper %s --replication-factor 1 --partitions 1 --topic %s" % (kafka_addr, topic)
            print(create_topic)
            os.system(create_topic)

        elif action == 'send':
            topic = sys.argv[2]
            send_topic = "bin\kafka-console-producer.sh --broker-list %s --topic %s" % (kafka_addr, topic)
            os.system(send_topic)

        elif action == 're':
            topic = sys.argv[2]
            re_topic = "bin\kafka-console-consumer.sh  --zookeeper %s  --topic %s --from-beginning" % (zk, topic)
            os.system(re_topic)
