import sys
import time
from functools import singledispatch


@singledispatch
def send(obj):
    print(obj)

@send.register(str)
def _(message):
    print(message)

if __name__ == '__main__':
    s = send(time.localtime(time.time()))
    s1 = send("1")

