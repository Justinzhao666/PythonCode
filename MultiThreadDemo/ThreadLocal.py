#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import threading

#这里就创建了一个ThreadLocal变量，这本质是一个dict。线程会自动根据自己的线程名获取自己的值
local = threading.local()

def process_student():
    std = local.student   #当调用这个取值的时候，会自动根据当前线程取出对应的数值
    print('Hello,%s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    local.student = name   #local像是一个未指明属性的对象，可以自己定制属性名称。 在赋值的时候自动将当前线程作为key赋值进去
    process_student()


t1 = threading.Thread(target=process_thread,args=('Justin',),name='Thread-1')
t2 = threading.Thread(target=process_thread,args=('Lucy',),name='Thread-2')

t1.start()
t2.start()

t1.join()
t2.join()

print('all end')