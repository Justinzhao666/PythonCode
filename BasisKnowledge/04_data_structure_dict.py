#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python中的数据结构-dict
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    dict 全称dictionary，即为Map，一种映射式的存储 key-value 元素结构，查找速度极其迅速！
    @因为通过函数映射关系，key直接通过hash算法运算出value的地址，所以算法复杂度可以达到常数级别！
    @key必须为不可变对象
    所谓的不可变对象指的是该变量的引用指向的 数据结构是不可变的！ 如 常数 str就是不可变的，list就是可变的

    和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 定义一个dict （大括号）

#获取值
d['Michael']        # dict根据key取值，key不存在报错
d.get('Thomas')     # key不存在返回None（什么都不会显示）
d.get('Thomas',-1)  # key不存在返回指定的值 -1

#添加值
d['Adam'] = 67  # dict放入新值

#修改值
d['Adam'] = 66  # = 66, 针对同一个key放入value，后来的会将前一个覆盖，其实就是重新赋值

#删除值
d.pop('Bob')    # 删除指定key的 key-value对

'Thomas' in d   # 判断dict中是否存在key




