import sys
import time


def hello():
    word = sys.argv[1]
    print ("hello " + word)

if __name__ == '__main__':
    s = str(time.time())
    print(s)
