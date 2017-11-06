#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from collections import namedtuple

#namedtuple, 相当于将一个tuple重新命名，并定义这个新的tuple的属性。然后像类一样的去使用它
Point  = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)


#deque非常高效地往头部添加或删除元素append and pop。 就是个双端队列
from collections import deque
q = deque(['a','b','c'])
q.append('d')
q.appendleft('o')
print(q)

#defaultdict：对dict的改进，针对于dict没有key的情况返回一个自己预定的值
from collections import defaultdict

dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])  #当dict的key为空时候返回自己预定义的值

#ordereddict,针对dict，依据key插入的顺序进行排序，先插入的排在前面。
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# Counter 计数器,是dict的子类： 统计一个字符的出现的次数--字符为dict的key，对于该字符的统计结果为value
from collections import Counter
c = Counter()
for ch in 'nihaoa,woshizhaohaoren':
    c[ch] = c[ch]+1
print(c)