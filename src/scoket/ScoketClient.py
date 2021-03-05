# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:46:33 2018

@author: lihc
"""

#==============================================================================
# 2. TCP client端代码
# #!/usr/bin/env python
# #
# # -*- coding:utf-8 -*-
# #
#==============================================================================

from socket import *

HOST='127.0.0.1'
PORT=21567
BUFSIZE=1024
ADDR=(HOST, PORT)

tcpCliSock=socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
if __name__ == '__main__':

    while True:
        # 手动输入:
        # data = input('>')
        data = "hello"
        print(type(data))
        print("消息发送: "+data)
        data = str.encode(data)
        if not data:
            break
        tcpCliSock.send(data)
        data=tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print (data)

    tcpCliSock.close()