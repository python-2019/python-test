import random
import time
import asyncio
from multiprocessing import Process

from src.kafka.KafkaProduct import get_msg, send

from src.util.mysqlUtil import mysqlUtil


def get_vin_array(single=False):
    if single:
        return ["LS7JSGVW1HB100004"]
    vins = [];
    conn = mysqlUtil.getConn("jmc_fleet")
    fetchmany = mysqlUtil.execute_and_fetchmany(conn, "select VIN_CODE from vehicle", 15000)
    for one in fetchmany:
        vins.append(one[0])
    return vins


def send_veh_status_all(topic="testTopic"):
    event = ["OFFLINE", "ONLINE", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER"]
    # event = ["OFFLINE", "ONLINE", "DRIVETIMER"]
    # topic = "veh.status.all"
    # topic = "vehicle-action-41"
    # topic = "testTopic"
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(10000):
        event_code = event[random.randint(0, event.__len__() - 1)]
        vins = get_vin_array()
        vin = vins[random.randint(0, vins.__len__() - 1)]
        msg = get_msg(vin, event_code)
        print(str(i) + "===" + str(event_code) + "===" + vin)
        # print(msg)
        send(topic, msg, kafka_addr)
        # time.sleep(0.1)


def send_veh_status_all_single(topic = "testTopic"):
    # topic = "veh.status.all"
    # topic = "testTopic"
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(1):
        msg = """{"id":"b4aeb9fc-1582185095449-09xx2","vin":"GPTESTN8062N00017","iccid":"89860919700028513675","imei":"864506031295695","veh_series":"CX743ICA","event_code":"ONLINE","recv_ts":1582185095468,"pkg_ts":1582617543451,"send_type":"0","pkg_id":"b4aeb9fc-1582185095449-0942","data":{"V998":{"sts":1,"val":"1582617543468"}}}
        """
        print(msg)
        send(topic, msg, kafka_addr)
        time.sleep(0.1)


def do_multiprocessing():
    p1 = Process(target=send_veh_status_all, args=())  # 有参数 必须加,号
    p2 = Process(target=send_veh_status_all, args=())
    p3 = Process(target=send_veh_status_all, args=())
    p4 = Process(target=send_veh_status_all, args=())
    p1.start()
    p2.start()
    p3.start()
    p4.start()


if __name__ == '__main__':
    # send_veh_status_all()
    # send_veh_status_all_single()
    # get_vin_array();
    do_multiprocessing()
