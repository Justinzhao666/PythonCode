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
        try -> except ... except -> else -> finally；
        logging模块；
        自定义异常类；
        raise 拋出异常；
'''

'''
    
    python 的异常也是一个对象：对象的基类为BaseException；
    异常其实就是程序在编译或者运行的时候，发现了非法的操作，因为这种非法的操作不能进行下去，于是在当前的地方，虚拟机会抛出一个对象，该对象就是异常对象；
    这个对象会一直向上抛出；
    
    注意：
    1. 异常会在发生处中断，不再向下执行;
    2. finally 总会执行;
    3. 如果异常不处理,只管向上抛出,最终会抛到虚拟机,最终导致程序终端;
    
'''


## 异常一般操作
def func(s):
    return 10 / int(s);
try:
    func(0)  # 异常点
    print('异常发生点之后的内容不被执行')
except Exception as e:
    logging.exception(e)  # logging模块可以非常容易地记录错误信息，通过配置可以将异常保存到文件中
    print('捕获异常:', e)
except ZeroDivisionError as e:
    print('上一级父级异常会捕获其所有子类异常，下面的子类就接收不到异常！', e)
else:
    print('没有异常就会执行else模块')
finally:
    print('finally 始终被执行')

# 如果捕获了异常就不会中断程序
print('发生异常后是否会中断程序')

print('--------------------------------')

## 抛出异常raise

# 异常如果不处理就会一直抛到虚拟机,然后终端程序!!!
# raise ValueError('满足条件可以在任意地方，主动去抛出异常')
def raiseException():
    try:
        func(0)
    except Exception as e:
        print('异常发生了')
        # raise # 表示什么都不做，为了调试使用！ 打出异常trace信息
        raise ValueError('raise在向上抛出的时候 可以改变异常类型，但是要慎重！')
# raiseException()

print('--------------------------------')

## 自定义异常
class MyException(BaseException): # 继承合适的异常类
    pass
def test(s):
    if s == 0:
       raise MyException('error:')
test(0)