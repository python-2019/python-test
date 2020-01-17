import sys
import time
from datetime import date
from functools import singledispatch


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

