import random
import time

from src.kafka.KafkaProduct import get_msg, send
import sys

from src.util.mysqlUtil import mysqlUtil


def get_vin_array(single=False):
    if single:
        return ["LS7JSGVW1HB100004"]
    vins = [];
    conn = mysqlUtil.getConn("jmc_fleet")
    fetchmany = mysqlUtil.execute_and_fetchmany(conn, "select VIN_CODE from vehicle", 10000)
    for one in fetchmany:
        vins.append(one[0])
    return vins


def send_veh_status_all():
    event = ["OFFLINE", "ONLINE", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER", "DRIVETIMER",
             "DRIVETIMER", "DRIVETIMER", "DRIVETIMER"]
    # event = ["OFFLINE", "ONLINE", "DRIVETIMER"]
    # topic = "veh.status.all"
    topic = "testTopic"
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(10000):
        event_code = event[random.randint(0, event.__len__() - 1)]
        vins = get_vin_array()
        vin = vins[random.randint(0, vins.__len__() - 1)]
        msg = get_msg(vin, event_code)
        print(str(i) + "===" + str(event_code) + "===" + vin)
        # print(msg)
        send(topic, msg, kafka_addr)
        time.sleep(0.1)


def send_veh_status_all_single():
    # topic = "veh.status.all"
    topic = "testTopic"
    kafka_addr = ["172.20.66.238:9092"]

    for i in range(1):
        msg = """{"id":"f11c6fc4-1582277433000-0952","vin":"GPTESTN8062N00003","iccid":"89860919700029832371","imei":"864506031283949","veh_series":"CX743ICA","event_code":"DRIVETIMER","recv_ts":1582277433000,"pkg_ts":1782277433000,"send_type":"0","pkg_id":"26cdd2e9-1582184313668-0458","data":{"V009":{"sts":0,"val":"1"},"V008":{"sts":0,"val":"0"},"V206":{"sts":1,"val":"0"},"V007":{"sts":0,"val":"-1"},"V006":{"sts":0,"val":"0"},"A029":{"sts":0,"val":"0"},"V052":{"sts":0,"val":"110"},"V171":{"sts":0,"val":"2"},"V170":{"sts":0,"val":"2"},"V015":{"sts":0,"val":"40000"},"V014":{"sts":0,"val":"0"},"V013":{"sts":0,"val":"0"},"V134":{"sts":0,"val":"0"},"V012":{"sts":0,"val":"0"},"V011":{"sts":0,"val":"0"},"V010":{"sts":0,"val":"0"},"V439":{"sts":1,"val":"0"},"V438":{"sts":1,"val":"0"},"V039":{"sts":0,"val":"0"},"A478":{"sts":0,"val":"0"},"A479":{"sts":0,"val":"0"},"A477":{"sts":0,"val":"0"},"A034":{"sts":1,"val":"0"},"A032":{"sts":1,"val":"0"},"V040":{"sts":0,"val":"0"},"A033":{"sts":1,"val":"0"},"A030":{"sts":1,"val":"0"},"A031":{"sts":1,"val":"0"},"V005":{"sts":1,"val":"0"},"V004":{"sts":1,"val":"0"},"V003":{"sts":1,"val":"0"},"V124":{"sts":1,"val":"0.0"},"V002":{"sts":1,"val":"0"},"V122":{"sts":1,"val":"0.0"},"V001":{"sts":0,"val":"11.4"},"V440":{"sts":1,"val":"0"},"V042":{"sts":0,"val":"0"},"P001":{"sts":1,"val":"0"},"P003":{"sts":1,"val":"0.0"},"V029":{"sts":1,"val":"0"},"P002":{"sts":1,"val":"0"},"V149":{"sts":1,"val":"0"},"V028":{"sts":0,"val":"0"},"V303":{"sts":0,"val":"0"},"V030":{"sts":1,"val":"0.0"},"V038":{"sts":1,"val":"0"},"V037":{"sts":1,"val":"-1"},"V036":{"sts":1,"val":"0"},"V035":{"sts":1,"val":"0"},"GPS003":{"sts":0,"val":"35.04731"},"V034":{"sts":1,"val":"0.0"},"GPS002":{"sts":0,"val":"104.26949"},"V032":{"sts":1,"val":"0"},"V031":{"sts":1,"val":"0.0"},"V019":{"sts":1,"val":"0.0"},"V018":{"sts":1,"val":"P"},"V017":{"sts":1,"val":"0"},"V138":{"sts":1,"val":"0"},"V148":{"sts":1,"val":"0"},"V027":{"sts":0,"val":"0"},"V147":{"sts":1,"val":"0"},"V026":{"sts":0,"val":"0"},"V146":{"sts":1,"val":"0"},"V025":{"sts":0,"val":"0"},"V145":{"sts":1,"val":"0"},"V024":{"sts":0,"val":"0.0"},"V023":{"sts":0,"val":"203.5"},"V067":{"sts":1,"val":"0"},"V022":{"sts":0,"val":"220.0"},"V021":{"sts":0,"val":"200.75"},"V186":{"sts":1,"val":"0"}}}
"""
        print(msg)
        send(topic, msg, kafka_addr)
        time.sleep(0.1)


if __name__ == '__main__':
    send_veh_status_all()
    # send_veh_status_all_single()
    # get_vin_array();
