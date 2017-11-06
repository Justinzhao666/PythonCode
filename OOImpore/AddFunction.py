#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from types import MethodType

class Student(object):
    # __slots__ = ('name','age','gender')
    pass


def setName(self,name):
    self.name = name

stu = Student()
stu.setName = setName
# stu.setName = MethodType(setName,stu)
stu.setName(stu,'zhao')
print(stu.name)


stu1 = Student()
stu1.gender = 'M'
print(stu1.gender)

