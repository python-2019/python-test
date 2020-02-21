import random
import time

from src.kafka.KafkaProduct import get_msg, send
import sys
sys.path.append("C:/AA--tima/code/test/python/python-test")
# sys.path.append("C:/AA--tima/code/test/python/python-test/kafka")
# sys.path.append("C:/AA--tima/code/test/python/python-test/kafka/tima")

def send_veh_status_all():
    event = ["OFFLINE", "ONLINE", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER"]
    # event = ["OFFLINE", "ONLINE", "DRIVETIMER"]
    vin = "LS7JSGVW1HB100004"
    topic = "veh.status.all"
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(10000):
        event_code = event[random.randint(0, event.__len__() - 1)]
        msg = get_msg(vin, event_code)
        print(str(i) + "===" + str(event_code))
        # print(msg)
        send(topic, msg, kafka_addr)
        time.sleep(0.1)


if __name__ == '__main__':
    send_veh_status_all()
