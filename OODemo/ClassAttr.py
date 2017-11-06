#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

class Student(object):
    name = 'Student'

stu = Student()
print(stu.name)
print(Student.name)
stu.name = 'zhao'
print(stu.name)
print(Student.name)
stu2 = Student()
print(stu2.name)

del stu.name #删除实例属性name， 就恢复了被覆盖的类属性
print(stu.name)