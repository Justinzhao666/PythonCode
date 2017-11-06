#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python中的数据结构-set
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    @ 要创建一个set，需要提供一个list作为输入集合
    @ set 无序 无重复的集合
    @ set 只能存入不可变对象@see 04_data_structure_dict.py
'''

s = set([1, 2, 3])  # 创建一个set，需要一个list作为输出集合

s = set([1, 1, 2, 2, 3, 3]) # = {1, 2, 3} set中重复元素被自动过滤

# 添加元素
s.add(4)    # set中添加元素，重复元素可以添加但是不会有效果
# 删除元素
s.remove(4) # set中删除元素

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2     # 交集 = {2, 3} ,set可以用来做集合运算
s1 | s2     # 并集 = {1, 2, 3, 4}

var = 10     # var为不可变对象
var1 = [10,2]# var1为可变对象
s.add(var)
print(s)

l = [1,2,8] # TypeError: unhashable type: 'list': list为可变对象，所以是unhashable对象
t = (5,6,7) # tuple为一个不可变对象 = {1, 2, 3, (5, 6, 7), 10}，于是存入整个对象---其实不变的是地址，所以会拿地址来计算
s.add(t)
print(s)