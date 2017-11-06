#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    控制台控制输入输出
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates


#获取控制台的输入


name = input('please input your name:')


#向控制台输出
print('hello',name)
print('100+200=',100+200)

print('%s格式化输出：%d' % ('this',1))
'''
    %s 将任何数据类型转换为字符串
    %d 表示数字
    %.2f 表示float字符，保留小数点后两位
    %% 表示%号
'''

data = input('<')
