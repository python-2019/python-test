# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:42:50 2018

@author: lihc
"""

# ==============================================================================
# 1. TCP server端代码
# #!/usr/bin/env python
# #
# # -*- coding:utf-8 -*-
# #
# ==============================================================================

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 60000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSrvSock = socket(AF_INET, SOCK_STREAM)
tcpSrvSock.bind(ADDR)
tcpSrvSock.listen(5)
if __name__ == '__main__':
    while True:
        print('waiting for connection ...', ctime())
        tcpCliSock, addr = tcpSrvSock.accept()
        print('... connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZE)
            print("接收消息: ", data)
            if not data:
                break
            tcpCliSock.send(str.encode('[%s] %s' % (ctime(), data)))
            print("回复消息: ",[ctime()], ':', data)

        tcpCliSock.close()
    tcpSrvSock.close()