#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：高阶函数 之 偏函数
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

'''
    functools.partial 提供了一个偏函数的功能
    其作用是：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

    偏函数就是用于将原来一个函数给他添加一些默认参数，从而形成一个新的函数。

    当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''

int('10000') # 将字符串转为int
int('10000',base=2) # 转为二进制数据

#此时如果我们需要一个函数 效果等同于int(xxx,base=2)，Python提供了一个简约的写法：
int2 = functools.partial(int,base=2)
int2('10000') # 生成的int2就是新的int的偏函数 = int('10000',base=2)
int2('10000',base=10) # base值可以继续被后续的赋值覆盖

