#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)#就相当于   def add(): xxxx
        return type.__new__(cls, name, bases, attrs) #返回一个类的定义

class MyList(list, metaclass=ListMetaclass):
    def output(self):
        print('hehehehehehe')
    pass

# class MyList(list):
#     def output(self):
#         print('hehehehehehe')
#     pass


list1 = MyList()
list1.output()


# list1.add(123)
# print(list1)
list1.output()


