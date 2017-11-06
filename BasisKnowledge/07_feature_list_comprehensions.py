#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：列表生成式
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    列表生成器是用于 花样的生成list
    ## 有了列表生成式就可以让通过for循环的生成list的代码直接用 [statement, for expression] 生成了。
    ## 当需要生成根据一些条件生成list的时候，首先考虑列表生成式！ 代码越少越好！
'''

# 普通用法：生成一串list
range(1,5)  # [1,2,3,4]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 格式 [ (要生成元素的表达式) (for 循环的内容)] [statement, for expression]
## 要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用。
print( [x * x for x in range(1,11)] ) # = [4, 16, 36, 64, 100]
## for循环中加入判断
print( [x * x for x in range(1, 11) if x % 2 == 0] )
## 双重for循环
print( [m + n for m in 'ABC' for n in 'XYZ' if n == 0] )
'''
     [m + n for m in 'ABC' for n in 'XYZ' if n % 2 == 0] 等同于

     for m in 'ABC':
        for n in 'XYZ':
            if n % 2 == 0:
                list.append(m + n)

'''

# 使用实例：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print( [k + '=' + v for k, v in d.items()] ) # = ['y=B', 'x=A', 'z=C']
import os
print( [d for d in os.listdir('.')] )