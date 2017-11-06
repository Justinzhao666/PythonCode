#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 启动大量的子进程的时候，使用进程池来批量创建子进程'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from multiprocessing import Pool
import os,time,random

def long_time_track(name):
    print('Run task %s(%s)...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))


if __name__ == '__main__':
    print('Parent process is %s'% os.getpid())
    p = Pool(4) #创建进程池,可以下一子创建4个进程
    for i in range(5): #连续创建4个进程，但是第5个要等到前四个进程某个结束后才会接着创建（容量为4）
        p.apply_async(long_time_track,args=(i,))
    print('Waiting for all sub processes done...')
    p.close() #关闭进程池，关闭后不能再向进程池中添加进程
    p.join() #让所有的子进程完成执行完毕后，执行下面程序
    print('All done')


