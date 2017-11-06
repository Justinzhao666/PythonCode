#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import threading,time

number = 0
lock = threading.Lock()  #创建一个锁，来锁住线程对数字操作的部分

def change_num(var):
    global number
    number = number +var
    number = number -var

def run_thread(n):
    #只要循环次数足够多，就会出现线程的乱窜导致的变量脏数据这种情况，线程本身就是轮番调度的
    for i in range(1000000):
        #首先要获取到锁
        lock.acquire()
        try:
            #放心操作数据
            change_num(n)
        finally:
            #操作结束了一定要释放锁，不然会让别的等待锁的线程一直在等！造成死线程现象
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
#线程是被cpu执行是指令级别的，一个语句会被拆成多个语句，这里就会发生读未提交等情况

t1.join()
t2.join()

print(number)