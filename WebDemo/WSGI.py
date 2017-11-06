#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

#这个程序运行 需要开启一个http服务器，类似于iis这些的用来对底层协议进行封装。让我们不用管处理的细节

def application(environ,start_response):
    # 响应的报头部分
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 响应的报体部分， 通过return来返回这些部分
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]