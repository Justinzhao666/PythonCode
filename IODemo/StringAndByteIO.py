#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from io import StringIO
from io import BytesIO

def opString():
    f = StringIO();
    f.write('hello')
    f.write(' ')
    f.write('world')
    print(f.getvalue())

    f1 = StringIO('fuck\nyou\nasshole!')
    while True:
        str = f1.readline()
        if str == '':
            break
        print(str)

def opByteIO():
    f = BytesIO('fuck\nyou\nbitch!'.encode('utf-8'))
    print(f.read())

    f.write(' yes'.encode('utf-8'))
    print(f.getvalue())

opByteIO()
opString()