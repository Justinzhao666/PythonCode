#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import os

#dir -l

def dirList():
    dict = [x for x in os.listdir('.')]
    print(dict)

dirList()


os.listdir('.')

def findFile(str,path='.'):
    for x in os.listdir(path):
        if os.path.isdir(x):
            findFile(str,os.path.join('.',x))
        elif x.__contains__(str):
            print(os.path.join(path,x),'\n')

findFile('py')