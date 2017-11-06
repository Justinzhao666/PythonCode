
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates
try:
    f = open('C:/Users/Administrator/Desktop/RainNumber.java','r')
    print(f.read())
finally:
    if f:
        f.close()

# 和上面是等价写法
with open('C:/Users/Administrator/Desktop/RainNumber.java','r') as f:
    print(f.read())

# for line in f.readlines():
#     print(line.strip())

