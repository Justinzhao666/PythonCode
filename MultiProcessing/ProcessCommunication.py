#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 创建两个进程，一个从queue中读数据一个从queue中写入数据'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates


from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('process to write: %s'% os.getpid())
    for val in ['A','B','C']:
        print('put %s into queue'%val)
        q.put(val)
        time.sleep(random.random())

def read(q):
    print('process to read:%s'%os.getpid())
    while True:  #不断地从Queue中读取数据
        val = q.get(True)
        print('get %s from queue'%val)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,)) #进程写
    pr = Process(target=read,args=(q,))  #进程读

    pw.start()
    pr.start()

    pw.join()  #写完了才能做其他的操作，等待pw结束
    pr.terminate() #pr中的是死循环，智能用terminate来强制终止