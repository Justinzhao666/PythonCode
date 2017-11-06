#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
#获取的这个资源好像只有一个，每次获取都是一样的

# task中有两个函数，就是一个个消息
# 自然会首先处理hello1()，当处理到sleep的时候需要等待，这时候有hello2()的出现，那就处理hello2()
# 当hello2()也遇到sleep的时候，这时候主线程中已经没有了了消息。那么就开始执行耗时操作了，直到其返回继续执行消息未完成的项。
# 消息是消息，打印输出是一个消息，但是函数就是函数，必须一条一条的执行，sleep结束后才能继续执行下面
# 一个函数整体为一个事件，loop对事件整体进行处理。处理不了整体后移，处理下一个函数，而不是在函数内部进行异步。

# 之前没有看好首先输出的是两个hello world，也就是说直接执行了两个hello()