import random
import time
from multiprocessing import Process

from src.kafka.KafkaProduct import get_msg, send
from src.util.dateUtil import dateUtil
from src.util.mysqlUtil import mysqlUtil

# test_kafka_addr = ["172.20.66.120:9092"]
test_kafka_addr = ["172.20.66.143:9092"]
uat_kafka_addr = ["jmctsphadoop03.uat:9092","jmctsphadoop04.uat:9092","jmctsphadoop05.uat:9092"]


# uat_kafka_addr = ["jmctsphadoop03.uat:9092,jmctsphadoop04.uat:9092,jmctsphadoop05.uat:9092"]

def get_msg(vin, event):
    str = """
    {"id":"a914fc63-c0de-40ad-b87d-527343403d35","vin":"%s","iccid":"","imei":"867223025100962","veh_series":"N520EV","event_code":"%s","recv_ts":1497841381408,"pkg_ts":1997841381408,"send_type":"0","data":{"A108":{"sts":0,"val":"0"},"V006":{"sts":0,"val":"0"},"A109":{"sts":0,"val":"0"},"A106":{"sts":0,"val":"0"},"A107":{"sts":0,"val":"0"},"A104":{"sts":0,"val":"0"},"A105":{"sts":0,"val":"0"},"A069":{"sts":0,"val":"0"},"A102":{"sts":0,"val":"0"},"A103":{"sts":0,"val":"0"},"A067":{"sts":0,"val":"0"},"A100":{"sts":0,"val":"0"},"A068":{"sts":0,"val":"0"},"A101":{"sts":0,"val":"0"},"A065":{"sts":0,"val":"0"},"A066":{"sts":0,"val":"0"},"A063":{"sts":0,"val":"0"},"A064":{"sts":0,"val":"0"},"A061":{"sts":0,"val":"0"},"A062":{"sts":0,"val":"0"},"A060":{"sts":0,"val":"0"},"V015":{"sts":0,"val":"0"},"A119":{"sts":0,"val":"0"},"A117":{"sts":0,"val":"0"},"A118":{"sts":0,"val":"0"},"A115":{"sts":0,"val":"0"},"A116":{"sts":0,"val":"0"},"A113":{"sts":0,"val":"0"},"A114":{"sts":0,"val":"0"},"A078":{"sts":0,"val":"0"},"A111":{"sts":0,"val":"0"},"A079":{"sts":0,"val":"0"},"A112":{"sts":0,"val":"0"},"E026":{"sts":0,"val":[{"sts":0,"val":"1"},{"sts":0,"val":"1"},{"sts":0,"val":"0"},{"sts":0,"val":"65496"},{"sts":0,"val":"0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"65496"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"}]},"A076":{"sts":0,"val":"0"},"A077":{"sts":0,"val":"0"},"A110":{"sts":0,"val":"0"},"A074":{"sts":0,"val":"0"},"A075":{"sts":0,"val":"0"},"A072":{"sts":0,"val":"0"},"A073":{"sts":0,"val":"0"},"A070":{"sts":0,"val":"0"},"A071":{"sts":0,"val":"0"},"V005":{"sts":0,"val":"0"},"V003":{"sts":0,"val":"0"},"V002":{"sts":0,"val":"0"},"V029":{"sts":0,"val":"0"},"A126":{"sts":0,"val":"0"},"E054":{"sts":0,"val":"1"},"A127":{"sts":0,"val":"0"},"E055":{"sts":0,"val":"3"},"A124":{"sts":0,"val":"0"},"E056":{"sts":0,"val":"0.0"},"A125":{"sts":0,"val":"0"},"E057":{"sts":0,"val":"1"},"A089":{"sts":0,"val":"0"},"A122":{"sts":0,"val":"0"},"E058":{"sts":0,"val":"3"},"A123":{"sts":0,"val":"0"},"E059":{"sts":0,"val":"0.0"},"V030":{"sts":0,"val":"0.0"},"A087":{"sts":0,"val":"0"},"A120":{"sts":0,"val":"0"},"A088":{"sts":0,"val":"0"},"A121":{"sts":0,"val":"0"},"A085":{"sts":0,"val":"0"},"A086":{"sts":0,"val":"0"},"A083":{"sts":0,"val":"0"},"A084":{"sts":0,"val":"0"},"A081":{"sts":0,"val":"0"},"A082":{"sts":0,"val":"0"},"A080":{"sts":0,"val":"0"},"V036":{"sts":0,"val":"0"},"V034":{"sts":0,"val":"0"},"V031":{"sts":0,"val":"0"},"V019":{"sts":0,"val":"0.0"},"V018":{"sts":0,"val":"0"},"V017":{"sts":0,"val":"65496"},"A098":{"sts":0,"val":"0"},"A010":{"sts":0,"val":"0"},"A099":{"sts":0,"val":"0"},"A096":{"sts":0,"val":"0"},"A097":{"sts":0,"val":"0"},"A094":{"sts":0,"val":"0"},"A095":{"sts":0,"val":"0"},"A092":{"sts":0,"val":"0"},"A093":{"sts":0,"val":"0"},"A090":{"sts":0,"val":"0"},"A091":{"sts":0,"val":"0"},"V143":{"sts":0,"val":"0"},"V052":{"sts":0,"val":"0"},"V051":{"sts":0,"val":"0"},"V050":{"sts":0,"val":"0"},"V056":{"sts":0,"val":"65496"},"V055":{"sts":0,"val":"0"},"V053":{"sts":0,"val":"0"},"E060":{"sts":0,"val":"1"},"E061":{"sts":0,"val":"5"},"E062":{"sts":0,"val":"65496"},"E063":{"sts":0,"val":"1"},"E064":{"sts":0,"val":"5"},"A038":{"sts":0,"val":"0"},"E065":{"sts":0,"val":"65496"},"A039":{"sts":0,"val":"0"},"V049":{"sts":0,"val":"0"},"V048":{"sts":0,"val":"0"},"A049":{"sts":0,"val":"0"},"E010":{"sts":0,"val":"0.0"},"E011":{"sts":0,"val":"0.0"},"A047":{"sts":0,"val":"0"},"A289":{"sts":0,"val":"0"},"E012":{"sts":0,"val":"0"},"A048":{"sts":0,"val":"0"},"E013":{"sts":0,"val":"0"},"A045":{"sts":0,"val":"0"},"A046":{"sts":0,"val":"0"},"E015":{"sts":0,"val":[{"sts":0,"val":"1"},{"sts":0,"val":"1"},{"sts":0,"val":"0.0"},{"sts":0,"val":"-1000.0"},{"sts":0,"val":"100"},{"sts":0,"val":"1"},{"sts":0,"val":"100"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"0.0"},{"sts":0,"val":"20"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"65496"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"},{"sts":0,"val":"0"}]},"A043":{"sts":0,"val":"0"},"A044":{"sts":0,"val":"0"},"A041":{"sts":0,"val":"0"},"A042":{"sts":0,"val":"0"},"A040":{"sts":0,"val":"0"},"GPS003":{"sts":0,"val":"28.51869"},"GPS002":{"sts":0,"val":"115.87848"},"A058":{"sts":0,"val":"0"},"E001":{"sts":0,"val":"0"},"A059":{"sts":0,"val":"0"},"E002":{"sts":0,"val":"65496"},"A056":{"sts":0,"val":"0"},"E003":{"sts":0,"val":"0"},"A057":{"sts":0,"val":"0"},"E004":{"sts":0,"val":"0.0"},"A054":{"sts":0,"val":"0"},"V063":{"sts":0,"val":"0"},"A055":{"sts":0,"val":"0"},"E006":{"sts":0,"val":"1"},"A052":{"sts":0,"val":"0"},"E007":{"sts":0,"val":"0"},"A053":{"sts":0,"val":"0"},"E008":{"sts":0,"val":"0"},"A050":{"sts":0,"val":"0"},"A292":{"sts":0,"val":"0"},"E009":{"sts":0,"val":"0"},"A051":{"sts":0,"val":"0"},"A293":{"sts":0,"val":"0"},"A291":{"sts":0,"val":"0"},"V065":{"sts":0,"val":"0"},"E075":{"sts":0,"val":"0"}}}
    """
    return str % (vin, event);


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
    event = ["DRIVETIMER"]
    topic = "veh.status.all"
    # topic = "vehicle-position-topic-41"
    # topic = "veh.dtc.data"
    # topic = "veh.status.allnew"
    # topic = "vehicle-action-41"
    # topic = "testTopic"

    for i in range(10000):
        event_code = event[random.randint(0, event.__len__() - 1)]
        vins = get_vin_array()
        vin = vins[random.randint(0, vins.__len__() - 1)]
        msg = get_msg(vin, event_code)
        print(str(i) + "===" + str(event_code) + "===" + vin)
        # print(msg)
        send(topic, msg, uat_kafka_addr)
        # time.sleep(1)


def send_veh_status_all_single(topic="testTopic"):
    topic = "veh.status.all"
    # topic = "veh.status.all.C01.test"
    # kafka_addr = test_kafka_addr
    kafka_addr = uat_kafka_addr
    print(topic)
    print(kafka_addr)
    for i in range(10000):
        # VINTEST0000000005 LS7FCGVC0HB000114
        msg = """{"id":"c83c0bf2-fdgf-dfgfdg-%d","vin":"CX743P326HN600064","iccid":"89860117770010373057","imei":"867223026862284","veh_series":"JH476","event_code":"DRIVETIMER","recv_ts":1587030371020,"pkg_ts":%d,"send_type":"0","pkg_id":"c83c0bf2-1587030371019-5665","data":{"V019":{"sts":0,"val":"90.0"},"V008":{"sts":0,"val":"0"},"V129":{"sts":1,"val":"0"},"V128":{"sts":1,"val":"0"},"V006":{"sts":0,"val":"0"},"V127":{"sts":1,"val":"0"},"A188":{"sts":0,"val":"0"},"A189":{"sts":0,"val":"0"},"V096":{"sts":0,"val":"0.0"},"A186":{"sts":0,"val":"7"},"V095":{"sts":0,"val":"1045.0"},"A187":{"sts":0,"val":"0"},"V094":{"sts":0,"val":"41"},"A184":{"sts":0,"val":"0"},"V093":{"sts":0,"val":"0.0"},"A185":{"sts":0,"val":"0"},"V092":{"sts":0,"val":"1039.5"},"A182":{"sts":0,"val":"2"},"V091":{"sts":0,"val":"38"},"A183":{"sts":0,"val":"0"},"V090":{"sts":0,"val":"0.0"},"A180":{"sts":0,"val":"0"},"A181":{"sts":0,"val":"0"},"V258":{"sts":1,"val":"0"},"V015":{"sts":3,"val":"0.0"},"V014":{"sts":0,"val":"0"}}}"""
        msg = msg % (dateUtil.timestamp_millis(), dateUtil.timestamp_millis())
        print(msg)
        print(i)
        try:
            send(topic, msg, kafka_addr)
        except Exception as e:
            print("发送异常: " + str(e))
        sleep = 5
        print("sleep: %ds" % sleep)
        time.sleep(sleep)
def send_veh_dtc_data_single(topic="testTopic"):
    topic = "veh.dtc.data"
    # topic = "veh.status.all.C01.test"
    # kafka_addr = test_kafka_addr
    kafka_addr = uat_kafka_addr
    print(topic)
    print(kafka_addr)
    for i in range(10000):
        # VINTEST0000000005 LS7FCGVC0HB000114
        msg = """{"pkg_id":"13b0ddf8-1597890178647-0651","vin":"LXWFEPHD6LT703348","iccid":"89860918710006512996","imei":"864687040927245","veh_series":"N520EV","event_code":"ENGINESTARTDIAGNOSTIC","recv_ts":%d,"pkg_ts":%d,"send_type":"0","ext_data":{},"data":{"0":{},"5":{"U012100":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U220D00":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U015500":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"B100116":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U010100":{"failure_type":"","dtc_prop":{"orgStu":"9"},"dtc_status":"9"},"U011200":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U011100":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U011000":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U121700":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U121800":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U107300":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U121600":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}},"6":{},"38":{},"39":{"U011000":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U007300":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}},"8":{},"12":{"C221000":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}},"13":{},"15":{"P1B0106":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U011101":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U007300":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P1B0101":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P1B011B":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U025902":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}},"18":{"P189916":{"failure_type":"","dtc_prop":{"orgStu":"40"},"dtc_status":"40"},"P184A16":{"failure_type":"","dtc_prop":{"orgStu":"40"},"dtc_status":"40"},"U029387":{"failure_type":"","dtc_prop":{"orgStu":"40"},"dtc_status":"40"},"P183519":{"failure_type":"","dtc_prop":{"orgStu":"44"},"dtc_status":"44"},"U107300":{"failure_type":"","dtc_prop":{"orgStu":"40"},"dtc_status":"40"}},"22":{"P140500":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P140900":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}},"23":{},"30":{"P21E093":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U0AC489":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21F190":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"U0AC4A0":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21F134":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21E0DD":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21E032":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21F011":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21E031":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"},"P21F131":{"failure_type":"","dtc_prop":{"orgStu":"8"},"dtc_status":"8"}}}}
"""
        msg = msg % (dateUtil.timestamp_millis(), dateUtil.timestamp_millis())
        print(msg)
        print(i)
        try:
            send(topic, msg, kafka_addr)
        except Exception as e:
            print("发送异常: " + str(e))
        sleep = 5
        print("sleep: %ds" % sleep)
        time.sleep(sleep)
def send_testTopic(topic="testTopic"):
    # topic = "testTopic2"
    topics = ["testTopic"]
    # topics = ["testTopic-1","testTopic2-1"]
    # kafka_addr = test_kafka_addr
    kafka_addr = uat_kafka_addr
    print(kafka_addr)
    for i in range(1):
        topic = topics[random.randint(0, topics.__len__() - 1)]
        print(topic)
        # VINTEST0000000005 LS7FCGVC0HB000114
        msg = """{"id":"c83c0bf2-%s","vin":"CX743P326HN600064","iccid":"89860117770010373057","imei":"867223026862284","veh_series":"JH476","event_code":"DRIVETIMER","recv_ts":1587030371020,"pkg_ts":%d,"send_type":"0","pkg_id":"c83c0bf2-1587030371019-5665","data":{"V019":{"sts":0,"val":"90.0"},"V008":{"sts":0,"val":"0"},"V129":{"sts":1,"val":"0"},"V128":{"sts":1,"val":"0"},"V006":{"sts":0,"val":"0"},"V127":{"sts":1,"val":"0"},"A188":{"sts":0,"val":"0"},"A189":{"sts":0,"val":"0"},"V096":{"sts":0,"val":"0.0"},"A186":{"sts":0,"val":"7"},"V095":{"sts":0,"val":"1045.0"},"A187":{"sts":0,"val":"0"},"V094":{"sts":0,"val":"41"},"A184":{"sts":0,"val":"0"},"V093":{"sts":0,"val":"0.0"},"A185":{"sts":0,"val":"0"},"V092":{"sts":0,"val":"1039.5"},"A182":{"sts":0,"val":"2"},"V091":{"sts":0,"val":"38"},"A183":{"sts":0,"val":"0"},"V090":{"sts":0,"val":"0.0"},"A180":{"sts":0,"val":"0"},"A181":{"sts":0,"val":"0"},"V258":{"sts":1,"val":"0"},"V015":{"sts":3,"val":"0.0"},"V014":{"sts":0,"val":"0"}}}"""
        msg = msg % (topic, dateUtil.timestamp_millis())
        print(msg)
        print(i)
        try:
            send(topic, msg, kafka_addr)
        except Exception as e:
            print("发送异常: " + str(e))
        sleep = 3
        print("sleep: %ds" % sleep)
        # time.sleep(sleep)

def send_reset_single(topic="testTopic"):
    topic = "veh.paak.reset"
    # kafka_addr = test_kafka_addr
    kafka_addr = uat_kafka_addr
    print(topic)
    print(kafka_addr)
    for i in range(1000):
        # VINTEST0000000005 LS7FCGVC0HB000114
        msg = """{"id":"c83c0bf2-1587030371019-5665","vin":"CX743P326HN600064","iccid":"89860117770010373057","imei":"867223026862284","veh_series":"JH476","event_code":"DRIVETIMER","recv_ts":1587030371020,"pkg_ts":%d,"send_type":"0","pkg_id":"c83c0bf2-1587030371019-5665","data":{"V500":{"sts":0,"val":"UHIJJINHIUHIHJKSHJKDHKJ"}}}"""
        print(msg % dateUtil.timestamp_millis())
        print(i)
        try:
            send(topic, msg % dateUtil.timestamp_millis(), kafka_addr)
        except Exception as e:
            print("发送异常: " + str(e))
        time.sleep(1)

def send_canal(topic="testTopic"):
    topic = "canal-ftb-tima-test"
    # kafka_addr = test_kafka_addr
    kafka_addr = uat_kafka_addr
    print(topic)
    print(kafka_addr)
    for i in range(1000):
        msg = """{"data":[{"id":"1","create_time":"2020-03-06 11:24:51","name":"rt","remark":"44444开发团队","update_time":"2020-03-02 16:37:51"}],"database":"tima-test","es":1603867843000,"id":1,"isDdl":false,"mysqlType":{"id":"bigint(20)","create_time":"datetime","name":"varchar(100)","remark":"varchar(100)","update_time":"datetime"},"old":[{"remark":"开发团队最666"}],"pkNames":["id"],"sql":"","sqlType":{"id":-5,"create_time":93,"name":12,"remark":12,"update_time":93},"table":"dept","ts":1603867843350,"type":"UPDATE"}"""
        print(msg)
        print(i)
        try:
            send(topic, msg , kafka_addr)
        except Exception as e:
            print("发送异常: " + str(e))
        time.sleep(1)

def send_tservice_unit_activation_topic():
    topic = "tservice-unit-activation-topic"
    kafka_addr = ["172.20.66.238:9092"]
    msg = """{"driverPhone":"18889899994","vin":"LS7JMGVN0HB100027"}"""
    send(topic, msg, kafka_addr)


def send_tservice_unit_open_topic():
    topic = "tservice-unit-open-topic"
    kafka_addr = uat_kafka_addr
    msg = """{"personLiablePhone":"13729000776","carBuyDepartment":"湛江顺铃汽车销售服务有限公司","authorizer":"刘璇","personLiable":"湛江顺铃汽车销售服务有限公司","authorizerMobile":"13729000776","carUseDepartment":"湛江顺铃汽车销售服务有限公司","vins":[{"VehSeriesName":"域虎9","vin":"LEFADDE19LTP01271","activationCode":"JPYmWY"}]}"""
    for i in range(1):
        send(topic, msg, kafka_addr)


def do_multiprocessing():
    p1 = Process(target=send_veh_status_all, args=())  # 有参数 必须加,号
    p2 = Process(target=send_veh_status_all, args=())
    p3 = Process(target=send_veh_status_all, args=())
    p4 = Process(target=send_veh_status_all, args=())
    p1.start()
    p2.start()
    p3.start()
    p4.start()


def send_flow_add_topic():
    topic = "flow.add.topic"

    for i in range(1):
        msg = """{"vin":"LMGFE6G88D1000001","iccid":"aojn"}"""
        msg = """{"vin":"JMCFACTORN806V201","iccid":"aojn"}"""
        print(msg)
        send(topic, msg, uat_kafka_addr)
        # send(topic, msg, test_kafka_addr)
        time.sleep(1)


if __name__ == '__main__':
    send_veh_status_all()
    # send_veh_status_all_single()
    # send_veh_dtc_data_single()
    # send_reset_single()
    # get_vin_array();
    # do_multiprocessing()
    # send_tservice_unit_activation_topic()
    # send_tservice_unit_open_topic()
    # send_flow_add_topic()
    # logstash 用
    # send_testTopic()
    send_canal()
