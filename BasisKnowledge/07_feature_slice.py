#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：切片
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    切片操作
    针对list 或者 tuple 或者string 进行元素的选取，取出数据中的部分数据
    list 切片后的数据依然是list
    tuple 切片后的数据依然是tuple
    string 切片后的数据依然是string
'''

L = [0,1,2,3,4,5,6,7,8,9]

# L [ begin : end : 间隔]
print(L[:])     # 等于原样list
print(L[0:3])   # [0,3)  取出 index 0 到 index3之前的所有数
print(L[:3])    # 如果是0开头，可以省略
print(L[-3:])   # 取出后三个，结束的index在最后可以不写
print(L[:10:2]) ## 前10个数，隔两个取出一个
print(L[::5])   # 所有数字，隔5个取出一个
print(L[::-1])  # 倒着数