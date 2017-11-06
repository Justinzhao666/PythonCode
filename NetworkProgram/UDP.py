#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import socket

# tcp是流式套接字，udp是数据包套接字，还有原始套接字啊啥的。
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

# 不需要listen() 方法！

# 直接不断的接受该符合该条件的数据包
while True:
    # 接收数据:返回数据和客户端的地址与端口
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 发送数据给客户端
    s.sendto(b'Hello, %s!' % data, addr)