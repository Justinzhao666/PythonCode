#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'通过枚举我们可以保证这是一个真正的常量'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 100 # Sun的value被设定为0
    Mon = 1
    Tue = 20
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun.value)
print(Weekday.Sun)
day = Weekday.Sun
print(day)

# can't set attribute,枚举后就不是变量了是真正的常量不可以改变
# Weekday.Sun.value =10
# print(Weekday.Sun.value)

