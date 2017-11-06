#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import os

print('system type : ',os.name)
# print('system info',os.uname())  windows上不提供该方法！
print('system environment : ',os.environ)
print('system environment by key : ',os.environ.get('PATH'))

print('absolute path',os.path.abspath('.'))
str = os.path.join(os.path.abspath('.'),'new_dir')
print('the whole path will be add:',str)
os.mkdir(str)
print('dir has been added')
os.rmdir(str)
print('dir has been removed')


