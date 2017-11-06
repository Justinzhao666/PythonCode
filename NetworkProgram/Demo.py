#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

HOST = '127.0.0.1'
PORT = 6666
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data)

tcpCliSock.close()