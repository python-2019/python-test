import os
import platform
import sys


"""
配置zk kafka地址
kafka安装路径(可配置环境变量)
"""
zk = "localhost:2181"
kafka_addr = "localhost:9092"
kafka_home = "C:\exe\kafka\kafka_2.12-2.1.1\\"


def sys_platform():
    if platform.system() == 'Windows':
        return 0
    if platform.system() == 'Linux':
        return 1


if __name__ == '__main__':
    sys_platform = sys_platform()
    env_kafka_home = os.getenv("KAFKA_HOME")
    if kafka_home is not None:
        print("kafka home: %s" % env_kafka_home)
        kafka_home = env_kafka_home+"\\"
    if sys_platform == 0:
        action = sys.argv[1]
        if action == 'list':
            list_zk = kafka_home + "bin\windows\kafka-topics.bat --zookeeper %s --list" % zk
            print(list_zk)
            os.system(list_zk)

        elif action == 'create':
            topic = sys.argv[2]
            create_topic = kafka_home + "bin\windows\kafka-topics.bat --create --zookeeper %s --replication-factor 1 --partitions 1 --topic %s" % (
            zk, topic)
            print(create_topic)
            os.system(create_topic)

        elif action == 'send':
            topic = sys.argv[2]
            send_topic = kafka_home + "bin\windows\kafka-console-producer.bat --broker-list %s --topic %s" % (
            kafka_addr, topic)
            print(send_topic)
            os.system(send_topic)

        elif action == 're':
            topic = sys.argv[2]
            re_topic = kafka_home + "bin\windows\kafka-console-consumer.bat  --zookeeper %s  --topic %s --from-beginning" % (
            zk, topic)
            print(re_topic)
            os.system(re_topic)

    elif sys_platform == 1:
        action = sys.argv[1]
        if action == 'list':
            s_list_zk = kafka_home + "bin\kafka-topics.sh --zookeeper %s --list" % zk
            os.system(s_list_zk)

        elif action == 'create':
            topic = sys.argv[2]
            create_topic = kafka_home + "bin\kafka-topics.sh --create --zookeeper %s --replication-factor 1 --partitions 1 --topic %s" % (
            zk, topic)
            print(create_topic)
            os.system(create_topic)

        elif action == 'send':
            topic = sys.argv[2]
            send_topic = kafka_home + "bin\kafka-console-producer.sh --broker-list %s --topic %s" % (kafka_addr, topic)
            os.system(send_topic)

        elif action == 're':
            topic = sys.argv[2]
            re_topic = kafka_home + "bin\kafka-console-consumer.sh  --zookeeper %s  --topic %s --from-beginning" % (
            zk, topic)
            os.system(re_topic)
