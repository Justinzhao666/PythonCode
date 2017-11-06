#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates


from wsgiref.simple_server import make_server
from WebDemo.WSGI import application


httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()