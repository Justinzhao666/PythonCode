#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python某些重要内置函数
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

#字符和对应整数码转换
ord('A') # = 65
chr(65) # = 'A'

# 转换编码
'ABC'.encode('ascii')
'中文'.encode('utf-8')
b'ABC'.decode('ascii') # = 'ABC' 将bytes数据转换为str

# 计算内容长度
len('中文') # =3
len(b'中文') # = 6 ，对于bytes计算字节数

# 生成list @see:BasisKnowledge/07_feature_list_comprehensions.py
range(1,5) # = 1,2,3,4,5 左闭右开 [1,5)的数据
list(range(5)) # = [0, 1, 2, 3, 4] ,range()生成一个整数序列 list()转换为list

#帮助信息
help(abs)  # 查看内置函数的帮助文档

# 类型转换
int('123')
float('12.34')
str(1.23)
bool(1)  # true
bool('') # false

# 判断是否为一个类型
isinstance('abc',str) # = true

# 获取一个对象的类型:可以判断基本数据类型，指向函数对象类型
type('abc')

# enumerate 将一个list转为索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

def function():
    pass
# 函数也是一个对象，自带一个__name__属性可以返回函数名
print(function.__name__)

# 比较重要的关键字 #
# in、pass、