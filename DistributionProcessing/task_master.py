#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import random,time,queue
#所对应的模块
from multiprocessing.managers import BaseManager

#创建两个队列，一个用于主进程放入任务给其他进程执行，一个队列用于其他进程执行的结果返回给主进程
# 创建用于进程间通信的队列,放入任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()


#关键部分：！！！！！！！
#继承BaseManager
class QueueManager(BaseManager):
    pass
# 1. 将本地Queue放入到网络中，注册到网络中，通过注册的函数获取对象
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
# 绑定端口5000, 设置验证码'abc'，start()启动
manager = QueueManager(address=('',5000),authkey=b'abc')
manager.start()
# 2.将网络中的Queue映射到本地上，这个是通过网络访问Queue对象的。
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放入任务
for i in range(10):
    n = random.randint(0,10000)
    print('Put task: %d'%n)
    task.put(n)
# 取出work进程执行的结果
for i in range(10):
    r = result.get(timeout=10)
    print('Result task:%s'%r)
# 关闭
manager.shutdown()
print('Master exit.')