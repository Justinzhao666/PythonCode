#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多线程和多进程  fork()函数在window下是无法使用的，windows不提供该接口'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import os

# os 为当前进程，os也是一个进程
print("process starting:(%s)",os.getpid())
# os fork()创建了一个子进程！
pid = os.fork()
if pid == 0:
    #
    print("i am child process(%s), and my parent is %s"%(os.getpid(),os.getppid()))
else:
    print("i(%s) create a child process(%s)"%(os.getppid(),pid))

