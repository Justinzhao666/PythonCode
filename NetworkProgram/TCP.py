#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import socket

# 创建套接字对象 (套接字ip协议ipv4,套接字类型tcp )
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 创建套接字连接,注意传入的参数
s.connect(('www.sina.com.cn', 80))

# 套接字通信，发送数据给服务器
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接受返回的数据，因为是流水式的慢慢发过来的，所以要慢慢接受while不断取取出数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data =  b''.join(buffer)

# 关闭连接
s.close()

# 处理所获取的数据
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
