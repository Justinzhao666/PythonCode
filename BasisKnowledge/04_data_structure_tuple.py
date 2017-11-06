#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python中的数据结构-tuple
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    tuple - 常量数组
    @tuple一旦初始化就不能修改。针对该数组只可读，不可修改。如果可能，能用tuple代替list就尽量用tuple
    @没有append()，insert()这样的方法。
'''

classmates = ('Michael', 'Bob', 'Tracy') # 定义一个tuple
t = ()      # 定义一个空的tuple
t = (1,)    # 定义一个元素的tuple，没有逗号就是普通的赋值

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
# tuple不可以改变，指的是tuple内部的引用的地址指向不可以变，但是指向的那块内存区域内容是可以修改的（如果那块内存区是list变量等这种结构的）
# a,b 为常量或者字符自然不能修改



