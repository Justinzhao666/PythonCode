#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from multiprocessing import Process
import os

#子进程要执行的函数
def run_proc(name):
    print('run child process %s (%s)'%(name,os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    #创建子进程,传入要执行的函数+ 参数 等等
    p = Process(target=run_proc, args=('test',))
    print('it will start the child process!')
    p.start()
    p.join()
    print('child process end')