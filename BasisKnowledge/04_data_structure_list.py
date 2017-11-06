#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python中的数据结构-list
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    list 是一个有序的集合，同list
'''

classmates = ['Michael', 'Bob', 'Tracy']    #定义一个列表
L = ['Apple', 123, True,['asp', 'php']]    #可以存储不同的数据类型

len(classmates) #求列表的长度 
len([]) # =0   

classmates[0]       #获取list的值、
classmates[0]='A'   #设置list的值


classmates[-1]  #获取倒数第一个值 -2，-3：倒数第二 倒数第三

classmates.append('Adam') #尾部添加元素
classmates.insert(1, 'Jack') #将元素插入指定位置

classmates.pop()    #尾部删除元素
classmates.pop(1)   #删除指定位置元素

[1,2,2,4].index(2) # 返回list第一个遇到值的索引，找不到则报错
