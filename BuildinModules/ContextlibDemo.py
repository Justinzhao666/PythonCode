#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import contextlib


# 包含有enter 和 exit 就是实现了上下文的管理  就可以使用with来提取对象

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin:')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('query info from %s'% self.name)


with Query('Bob') as q:
    q.query()

qq = Query('you')
qq.query()

# contextmanager,使用__enter__，__exit__还是太麻烦
from contextlib import contextmanager

class Query2(object):
    def __init__(self,name):
        self.name = name
    def query(self):
        print('Query from %s'%self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Jack') as q:
    q.query()

#  这个装饰器，是将contextmanager传进来，然后对其修改。会形成一个新的tag函数。======我估计是加上了__enter__，__exit__ 所以可以直接使用with
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield  #yield会将with后面的变量输出去
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


# closing  它的作用就是把任意对象变为上下文对象，并支持with语句。
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)