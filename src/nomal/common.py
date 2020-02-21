import time
from functools import singledispatch

from src.util.dateUtil import dateUtil


@singledispatch
def send(obj):
    print(obj)

@send.register(str)
def _(message):
    print(message)


def getDate():
    global strTime
    timeStamp = time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)


if __name__ == '__main__':
    getDate()
    print(strTime)
    date_str = dateUtil.get_now_date_str()
    print(date_str)
