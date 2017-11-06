#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    @ author    zhaohaoren
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

import logging

'''
    目录：
        print 打印
        assert 断言
        logging *
        pdb
        IDE **
        
    调试程序的几种方式： 直接使用IDE就ok了，不需要使用其他的那么麻烦！

'''

## assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' # 如果前面判断为Flase，就输出后面
    return 10 / n
# python3 -O err.py 加上-O 关闭执行断言！


## logging
'''
logging 其实就是将异常和错误等信息，保存给自己，然后输出。 其实就是log工具！

logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别;
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
'''
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    logging.info('info: n is %d'%n)
    return 10 / n


## pdb
# python3 -m pdb err.py
import pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# $ python3 -m pdb err.py 单步调试，一行一行的调试；
# 加上了pdb.set_trace() 可以使用python err.py。当运行到set_trace()的时候中断！
# 在终端的地方使用【p 变量名】可以查看运行中变量的值；

## 最好的调试：使用IDE