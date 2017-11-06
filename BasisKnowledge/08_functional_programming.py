#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：函数式编程,map,reduce
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    函数式编程的一个特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
    纯函数式编程调用链都是函数，Python可以使用变量 -> Python不是纯函数式编程语言。
    @ 函数式编程因为没有临界资源所以不会存在并发问题！

    Python中 函数名 其实是指向函数的变量，函数名也可以作为变量
'''

## 高阶函数，就是函数的参数能够接收别的函数。add就是一个高阶函数。
# 函数名当做变量，变量可以指向函数。然后当做函数使用。
f = abs
print(f(-10))  # = abs(-10) = 10

def add(x, y, f): # 既然是变量 就可以当做参数进行传递（当某个函数完成某些功能的时候需要其他函数参与的时候使用）
    return f(x) + f(y)


## map
# map(f,[x1, x2, x3, x4]) = f(x1),f(x2),f(x3),f(x4)
# map(函数，iterable对象)，return Iterator对象。
# 将传入的函数作用于iterable对象中每一个元素。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
next(r) # 取出一个元素
list(r) # 将迭代对象转为list

## reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# f需要接受两个参数，并将f运算的结果并入下一个数字的运算。
from functools import reduce
# 例子： 将数字的string转为int
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

## filter
# filter(f,[x1, x2, x3, x4]) = x1,x4
# 用于过滤序列,f是一个返回值为bool类型的函数，filter只保留序列中返回值为true的元素
def is_odd(n):
    return n % 2 == 1
# 例子：筛选出序列中的奇数
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


## sorted
# 排序算法
# 接受key 按key要求进行排序,key是一个函数，将作用于list每个元素！然后根据计算出来的结果排序，在讲排序结果修改为原来的值
print(sorted([36, 5, -12, 9, -21], key=abs))
# 字符串按照ASCII码来排序,key指定不区分大小写,reverse指定排序顺序反向排序，key可以是自己定义函数，用来作用于序列
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True)

## 匿名函数
# 直接将函数体传入
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# 直接返回函数体
def build(x, y):
    return lambda: x * x + y * y

