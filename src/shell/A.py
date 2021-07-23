# coding=utf-8
import os

if __name__ == '__main__':
    dir = "C:\AA--tima\code\\tima\jmc-b-tsp-sp\codeProject\\tdata-sync"
    os.chdir(dir)
    os.system("git branch")
    os.system("git pull http://git.timacloud.cn/jmc-b-tsp-sp/tdata-sync.git ")
