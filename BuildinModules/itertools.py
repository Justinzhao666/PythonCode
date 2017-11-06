#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import itertools

# count()  生成一个会无限的迭代器
natural = itertools.count(1)
# for n in natural:
#     print(n)

# 因为是可以无限迭代的，通过takewhile() 来截取指定数量的有限序列
ns = itertools.takewhile(lambda x: x <= 10, natural)
list(ns)

# cycle() 生成一个会不断循环的迭代里面的字符的迭代器
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# repeat() 不断重复一个数字，后面的数字可以指定重复的数字个数
ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

# chain()  组合迭代器，可以将两个容器 合并成一个大的迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)

# groupby() 将被迭代的容器根据相邻的相同的元素进行分组
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# 可以传入一个函数，并作用于被迭代的容器！
for key,group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key,list(group))


