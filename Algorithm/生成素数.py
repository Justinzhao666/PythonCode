#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    生成素数序列
    思路：
    从一个序列第一个元素开始，将整个序列除以这个值，如过除尽那么那个数就不是素数，从队列中去除
    此时的下一个元素肯定是素数，接着用下一个元素继续除，去除掉可以被除尽的数字，以此类推。
    @ author    Justin Zhao
    @ date      2018/1/1
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

# 预先生成奇数序列： 除2外，素数肯定不是偶数
def odd_maker():
    n = 1
    while True:
        n = n+2
        yield n #弄成生成器

# n为当前素数，x为list中的元素，将list元素除以n，如果除得0 那么x肯定不是素数，通过下面的filter将其去除
def filter_rule(n):
    return lambda x:x%n !=0

def primes():
    # 第一个素数为2
    yield 2
    list = odd_maker()
    while True:
        n = next(list)
        yield n # 生成器，生成素数
        list = filter(filter_rule(n),list)


for n in primes():
    if n>100: # 100以内的素数
        break
    else:
        print(n)