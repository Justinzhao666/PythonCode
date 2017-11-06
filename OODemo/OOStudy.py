#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates


class Student(object):
    #相当于构造函数，self不需要传入，self就表示该对象。
    def __init__(self,name,score,gender):
        self.name = name
        self.score = score
        self.__gender= gender
    def getvalue(self):
        print('%s,%s,%s'%(self.score,self.name,self.__gender))


stu = Student('zhao',10,'M')
print("对象",stu)
print("class name :",Student)
print("object value:"+ stu.name,stu.score)


#可以绑定任何属性变量
stu.age = 100
print(stu.age)

#使用其他方法
stu.getvalue()

# print(stu.__gender) error!

print(dir('ABC'))