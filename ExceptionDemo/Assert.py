#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import logging
logging.basicConfig(level=logging.INFO)
b
#assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
foo('0')



#logging
# s = 0
# n = int(s)
# logging.info('n = %d'%n)
# print(10/n)