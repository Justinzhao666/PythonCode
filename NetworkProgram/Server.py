#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'


__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import socket,threading,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 服务器端为绑定这个端口
s.bind(('127.0.0.1', 9998))
# 绑定完了 转为listen状态
s.listen(5) # 5代表等待连接的最大连接数
print('Waiting for connection...')


# 新线程的处理函数：
def tcplink(sock, addr):
    # 这个是在服务器端打印出来的
    print('Accept new connection from %s:%s...' % addr)
    # 这个就是socket通信，向客户端发消息
    sock.send(b'Welcome!')
    # 然后就处于了通信状态，一直等客户端发送过来数据就可以了
    while True:
        data = sock.recv(1024)
        #等待下，可以看过程
        time.sleep(1)
        # 检测什么时候是断开连接的
        if not data or data.decode('utf-8') == 'exit':
            break
        # 将文本原样+hello返回
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # 客户端请求断开连接，那么久应该关闭socket
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 开始不断地监听获取连接
while True:
    # 接受一个连接： 这个方法在没有连接的时候会一直在等待！
    sock,addr = s.accept()
    # 创建一个线程来处理TCP连接，每一个连接都要创建一个进程或者线程
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
