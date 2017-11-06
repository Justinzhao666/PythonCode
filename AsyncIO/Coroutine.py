#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 协程： 两个程序可以在任意时候切换，但是不是线程间的切换，而是相互协作的切换 \
  协程的实现是通过generator来实现的\
  #这个例子不好：协程弄的和子程序一样子'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

def consumer():
    r = ''
    while True:
        n = yield r # yield接受来自producer的数据 进行处理
        if not n:
            return
        print('[Consumer] Consuming %s'%n)
        r = '200 OK'  #这里处理结果为ok 会通过yield继续被返回出去

def producer(c):
    c.send(None)  #启动生成器
    n = 0
    while n < 5:
        n = n+1
        print('[Producer] Producing %s'%n)
        # 协程的意义： 在这里就会跳出去，执行别的程序，别的程序执行后又回来执行本程序。
        r = c.send(n)  # 每生成一个 就切换到consumer  c.send(n)：将n送到consumer将由yield来接受
        print('[Producer] Consumer return: %s'% r)
    c.close() # 关闭consumer

c = consumer()
producer(c)