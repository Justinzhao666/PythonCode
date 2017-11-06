#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：迭代,迭代器
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
from collections import Iterable, Iterator

'''
    给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
    Python中，迭代是通过for ... in来完成的，而不是java中的for循环list的下标来取值。
    for可以作用在任何可迭代对象上，比如：list，tuple，dict，string等

'''

# 判断是否为迭代对象
isinstance('abcd',Iterable)


# dict的迭代
dict = {'a':1,'b':2}
## 迭代key(默认迭代key)
for key in dict:
    print(key)
## 迭代value
for value in dict.values():
    print(value)
## 同时迭代
for k,v in dict.items():
    print(k + " " + v)


# 迭代中同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# output: 1,1 | 2,4 | 3,9

'''
    迭代器：Iterator （注意区分 迭代器，可迭代的概念）

    ## 可迭代对象：Iterable，这些可以直接作用于for循环的对象。
    可以直接作用于for循环的数据类型有以下几种：（他们都是可迭代的）
        一类是集合数据类型，如list、tuple、dict、set、str等；
        一类是generator，包括生成器和带yield的generator function。

    ## 迭代器：Iterator，可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
    ## generator 生成器都是迭代器对象，但list、dict、str是Iterable（可迭代的），却不是Iterator。

    ## 简要的说：可以for的是可迭代对象，可以next()的是迭代器

    ## Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
    # 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
    # Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

'''
isinstance([], Iterator) # = False list是可迭代的但是不是迭代器，（可以for，但无法使用next）
isinstance((x for x in range(10)), Iterator) # = True generator是迭代器

## 将list等可迭代的转为迭代器 iter(list...)
isinstance(iter([]), Iterator)