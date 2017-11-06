#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    基本数据类型介绍
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

# 整数 没有大小限制
number = 1

# 浮点数 没有大小限制 超出一定范围表示为inf
number_float = 1.23

# 字符串
str = 'hello'  + "i'am justin," + ' i\'am learning \"python\" \n' + '''
python is good
python is simple
....
''' + r'\\ \\ \\' #r 让''内不转义
str = b'abc' # bytes字符串，每个字符只占一个字节

str.replace('a','c') # 字符串替换函数

"""
    编码问题：
        因为一个文字所占字节数的不一致，导致了文字有很多编码：英文编码（ASCII编码，1字节），日文编码，中文编码等等
        @Unicode:
        Unicode统一了这些编码，两个字节表示一个字符，生僻字用4个字节。可以表示全球所有的文字
        Unicode对于某些字符来说太占空间了，---->出现了UTF-8（可变长的Unicode）
        @UTF-8：
        UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
        常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

    @ 在最新的Python 3版本中，字符串是以Unicode编码的，所以可以支持多字符

    具体用法@see: 06_function_buildin.py
"""



# 布尔值
is_flag1 = True
is_flag2 = False
is_flag1 or is_flag2 # = True
is_flag1 and is_flag2 # = False
not True # false

# 空值
null = None

# 变量 动态语义，a只是一个变量，可以任意指向数据类型（Python将任何数据都看成对象，变量指向对象）
a = 1
a = 'a'
a = False

# 常量 大写：代表这个是常量但是可以修改，只是概念上的常量
PI = 3.14159265359







