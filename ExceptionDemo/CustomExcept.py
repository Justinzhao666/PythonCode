#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError("invalid value %s"% s)
#     return 10/n
#
# foo(0)



def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()