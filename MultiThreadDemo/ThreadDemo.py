#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import time,threading

def loop():
    print('thread %s is running...'%threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is end'%threading.current_thread().name)
print('current thread is %s'% threading.current_thread().name)
#创建线程
t = threading.Thread(target=loop,name='LoopThread')
#开启线程
t.start()
#让线程执行完再说
# t.join()
print('thread %s is end'%threading.current_thread().name)
