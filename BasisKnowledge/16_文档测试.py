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

'''
    目录：
        doctest；
    简介：
        Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
        可以用...表示中间一大段烦人的输出。
'''


def fact(n):
    '''
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(3)
    6
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod() # 主要就是执行这个

# 直接运行该文件不会有任何问题！ 因为文档注释里面的输入和预期的输出结果一致，表明模块是正确的！
# 如果想输出，只要修改文档注释里面的输出值就可以了！就会报出模块问题！