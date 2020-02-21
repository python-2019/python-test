# -*- coding: utf-8 -*-
import time
from functools import singledispatch
import random

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


def get_msg(vin, event):
    str = """
    {"id":"a914fc63-c0de-40ad-b87d-527343403d35","vin":"%s","iccid":"","imei":"867223025100962","veh_series":"N520EV","event_code":"%s","recv_ts":1497841381408,"pkg_ts":1997841381408,"send_type":"0","data":{"A108":{"sts":0,"val":"0"},"V006":{"sts":0,"val":"0"},"A109":{"sts":0,"val":"0"},"A106":{"sts":0,"val":"0"},"A107":{"sts":0,"val":"0"},"A104":{"sts":0,"val":"0"},"A105":{"sts":0,"val":"0"},"A069":{"sts":0,"val":"0"},"A102":{"sts":0,"val":"0"},"A103":{"sts":0,"val":"0"},"A067":{"sts":0,"val":"0"},"A100":{"sts":0,"val":"0"},"A068":{"sts":0,"val":"0"},"A101":{"sts":0,"val":"0"},"A065":{"sts":0,"val":"0"},"A066":{"sts":0,"val":"0"},"A063":{"sts":0,"val":"0"},"A064":{"sts":0,"val":"0"},"A061":{"sts":0,"val":"0"},"A062":{"sts":0,"val":"0"},"A060":{"sts":0,"val":"0"},"V015":{"sts":0,"val":"0"},"A119":{"sts":0,"val":"0"},"A117":{"sts":0,"val":"0"},"A118":{"sts":0,"val":"0"},"A115":{"sts":0,"val":"0"},"A116":{"sts":0,"val":"0"},"A113":{"sts":0,"val":"0"},"A114":{"sts":0,"val":"0"},"A078":{"sts":0,"val":"0"},"A111":{"sts":0,"val":"0"},"A079":{"sts":0,"val":"0"},"A112":{"sts":0,"val":"0"},"E026":{"sts":0,"val":[{"sts":0,"val":"1"},{"sts":0,"val":"1"},{"sts":0,"val":"0"},{"sts":0,"val":"65496"},{"sts":0,"val":"0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"65496"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"}]},"A076":{"sts":0,"val":"0"},"A077":{"sts":0,"val":"0"},"A110":{"sts":0,"val":"0"},"A074":{"sts":0,"val":"0"},"A075":{"sts":0,"val":"0"},"A072":{"sts":0,"val":"0"},"A073":{"sts":0,"val":"0"},"A070":{"sts":0,"val":"0"},"A071":{"sts":0,"val":"0"},"V005":{"sts":0,"val":"0"},"V003":{"sts":0,"val":"0"},"V002":{"sts":0,"val":"0"},"V029":{"sts":0,"val":"0"},"A126":{"sts":0,"val":"0"},"E054":{"sts":0,"val":"1"},"A127":{"sts":0,"val":"0"},"E055":{"sts":0,"val":"3"},"A124":{"sts":0,"val":"0"},"E056":{"sts":0,"val":"0.0"},"A125":{"sts":0,"val":"0"},"E057":{"sts":0,"val":"1"},"A089":{"sts":0,"val":"0"},"A122":{"sts":0,"val":"0"},"E058":{"sts":0,"val":"3"},"A123":{"sts":0,"val":"0"},"E059":{"sts":0,"val":"0.0"},"V030":{"sts":0,"val":"0.0"},"A087":{"sts":0,"val":"0"},"A120":{"sts":0,"val":"0"},"A088":{"sts":0,"val":"0"},"A121":{"sts":0,"val":"0"},"A085":{"sts":0,"val":"0"},"A086":{"sts":0,"val":"0"},"A083":{"sts":0,"val":"0"},"A084":{"sts":0,"val":"0"},"A081":{"sts":0,"val":"0"},"A082":{"sts":0,"val":"0"},"A080":{"sts":0,"val":"0"},"V036":{"sts":0,"val":"0"},"V034":{"sts":0,"val":"0"},"V031":{"sts":0,"val":"0"},"V019":{"sts":0,"val":"0.0"},"V018":{"sts":0,"val":"0"},"V017":{"sts":0,"val":"65496"},"A098":{"sts":0,"val":"0"},"A010":{"sts":0,"val":"0"},"A099":{"sts":0,"val":"0"},"A096":{"sts":0,"val":"0"},"A097":{"sts":0,"val":"0"},"A094":{"sts":0,"val":"0"},"A095":{"sts":0,"val":"0"},"A092":{"sts":0,"val":"0"},"A093":{"sts":0,"val":"0"},"A090":{"sts":0,"val":"0"},"A091":{"sts":0,"val":"0"},"V143":{"sts":0,"val":"0"},"V052":{"sts":0,"val":"0"},"V051":{"sts":0,"val":"0"},"V050":{"sts":0,"val":"0"},"V056":{"sts":0,"val":"65496"},"V055":{"sts":0,"val":"0"},"V053":{"sts":0,"val":"0"},"E060":{"sts":0,"val":"1"},"E061":{"sts":0,"val":"5"},"E062":{"sts":0,"val":"65496"},"E063":{"sts":0,"val":"1"},"E064":{"sts":0,"val":"5"},"A038":{"sts":0,"val":"0"},"E065":{"sts":0,"val":"65496"},"A039":{"sts":0,"val":"0"},"V049":{"sts":0,"val":"0"},"V048":{"sts":0,"val":"0"},"A049":{"sts":0,"val":"0"},"E010":{"sts":0,"val":"0.0"},"E011":{"sts":0,"val":"0.0"},"A047":{"sts":0,"val":"0"},"A289":{"sts":0,"val":"0"},"E012":{"sts":0,"val":"0"},"A048":{"sts":0,"val":"0"},"E013":{"sts":0,"val":"0"},"A045":{"sts":0,"val":"0"},"A046":{"sts":0,"val":"0"},"E015":{"sts":0,"val":[{"sts":0,"val":"1"},{"sts":0,"val":"1"},{"sts":0,"val":"0.0"},{"sts":0,"val":"-1000.0"},{"sts":0,"val":"100"},{"sts":0,"val":"1"},{"sts":0,"val":"100"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"20"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"}]},"A043":{"sts":0,"val":"0"},"A044":{"sts":0,"val":"0"},"A041":{"sts":0,"val":"0"},"A042":{"sts":0,"val":"0"},"A040":{"sts":0,"val":"0"},"GPS003":{"sts":0,"val":"28.51869"},"GPS002":{"sts":0,"val":"115.87848"},"A058":{"sts":0,"val":"0"},"E001":{"sts":0,"val":"0"},"A059":{"sts":0,"val":"0"},"E002":{"sts":0,"val":"65496"},"A056":{"sts":0,"val":"0"},"E003":{"sts":0,"val":"0"},"A057":{"sts":0,"val":"0"},"E004":{"sts":0,"val":"0.0"},"A054":{"sts":0,"val":"0"},"V063":{"sts":0,"val":"0"},"A055":{"sts":0,"val":"0"},"E006":{"sts":0,"val":"1"},"A052":{"sts":0,"val":"0"},"E007":{"sts":0,"val":"0"},"A053":{"sts":0,"val":"0"},"E008":{"sts":0,"val":"0"},"A050":{"sts":0,"val":"0"},"A292":{"sts":0,"val":"0"},"E009":{"sts":0,"val":"0"},"A051":{"sts":0,"val":"0"},"A293":{"sts":0,"val":"0"},"A291":{"sts":0,"val":"0"},"V065":{"sts":0,"val":"0"},"E075":{"sts":0,"val":"0"}}}
    """
    return str % (vin, event);

if __name__ == '__main__':
    event = ["OFFLINE", "ONLINE", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER"]
    # event = ["OFFLINE", "ONLINE", "DRIVETIMER"]
    vin = "LS7JSGVW1HB100004"
    topic = "veh.status.all"
    # topic = "testTopic-batch"
    # topic = "testTopic-roll"
    # topic = "testTopic"
    # message = """{"date":"%s"}"""
    # message = """{"vin":"LS7JSGVW1HB100004","event_code":"ONLINE","date":"%s","recv_ts":"12361273623"}"""
    # kafka_addr = ["localhost:9092"]
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(10000):
        timeStamp = time.time()
        localTime = time.localtime(timeStamp)
        # strftime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        # print(message % strftime)
        event_code = event[random.randint(0, event.__len__() - 1)]
        msg = get_msg(vin, event_code)
        print(str(i) + "===" + str(event_code))
        # print(msg)
        send(topic, msg, kafka_addr)
        time.sleep(0.1)
