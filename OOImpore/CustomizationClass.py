#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates


class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self): #定制输出 对象的信息
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__  #调试用的输出写法，简易写法

print(Student('zhao'))
stu = Student('nick')

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self): # 实例本身就是迭代对象，故返回自己
        return self
    def __next__(self): #对其实例迭代，通过该next函数不断的取值。
        self.a ,self.b = self.b , self.a+self.b
        if self.a > 1000:
            raise StopIteration() #raise用于抛出一个异常
        return self.a
    def  __getitem__(self, item):
        if isinstance(item,int): #item传入的是一个索引
            a,b = 1,1
            for var in range(item):
                a,b = b,a+b
            return a
        if isinstance(item,slice): #item传入的是一个切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1,1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L

for var in Fib():
    print(var) #所以这里打印的是next的返回值
f = Fib()
print(f[0])
print(f[:5])