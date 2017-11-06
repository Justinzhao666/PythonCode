#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python面向对象的关键字
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

'''
    __slots__变量
    @property
    多继承
    __len__() :作用域len函数
    __repr__ 和 __str__ :相当于toString()
    __iter__ 和 __next__ :让类对象可迭代！
    __getitem__ ： 让类对象具有list行为和切片
    __getattr__ ： 提供当访问类中不存在的属性和方法的处理机制
    __call__：将一个对象当做方法来调用
    枚举
    type()：动态创建类
    元类
'''

## __slots__来限制class对象能在类外添加的属性和方法。（只对当前类有作用，对子类没有作用）
class MyClass(object):
    __slots__ = ('name','age') #MyClass的对象只能添加这两个属性，不能再添加其他关键字的了。

mc = MyClass();
mc.name = 'zhaohaoren'
mc.age = 20
# mc.gender = 'man' # 不能定义gender属性，被__slots__限制了。
## 如果子类里面也定义了__slots__，只要定义了，那么子类的限制属性就是子类的__slots__+ 父类的__slots__。


## @property
# 当我们使用get/set进行参数校验的时候，使用方法来获取值，这样还是不够方便，为什么不能直接访问属性，同时保证属性自带参数校验功能呢？
# @property装饰器就是处理上述情况，负责把一个方法变成属性调用的！

class Student(object):
    @property # 装饰get方法，在装饰@property的同时，会为其自动添加一个age.setter的装饰。
    def age(self): # 该函数在外部可以直接把方法当做属性来使用。
        return self._age
    @age.setter
    def age(self,value): ## 通过setter修饰，在给age赋值的时候会做参数校验。
        #做一些校验工作。
        self.age = value
    @property
    def name(self): # 只写property，不写set的话就是只读属性。
        return self.name
stu = Student()
stu.age # 直接访问方法的方式访问属性

## Python是可以使用多继承的,通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Derive(MyClass,Student):
    pass
# 当父类有方法重复的时候，按照继承顺序，先入为主，选用最先继承的那个类的方法。

## __len__
# __len__()方法我们也知道是为了能让class作用于len()函数。


## __repr__ 和 __str__
# __str__相当于java中的toString，print(object)会调用__str__。
# 但是，直接执行object调用的是__repr__，这个是为程序调试服务的。
# 一般这样写就行了：
class Student2(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__ # 共用一个方法
stu2 = Student2()
stu2
print(stu2)


## __iter__ 和 __next__
# __iter__ 返回一个迭代对象
# __next__ 被for in作用的时候，调用这个方法获取该值
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
for n in Fib():
    print(n)


## __getitem__
# __iter__只是可以让对象可以被迭代，但是不能保证他可以像list那样获取值，以及切片功能。
# __getitem__ 让对象可以像list一样被迭代和切片
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引 Fib()[i]
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片 Fib()[i:j]
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
## 如果希望对象和dict一样，就要修改__getitem__为dict想要的。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


## __getattr__
# 对用户试图访问不存在的属性或方法的处理！
class Student3(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score': # 返回值
            return 99
        if attr == 'age': # 返回函数
            return lambda: 25
Student3().score # 当调用score的时候，当发现类中不存在该属性的时候，就到__getattr__中找这属性。
## 作用：把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。：REST API--可以另做了解

## __call__
# 将对象看出函数来调用
class Student4(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s() # 将函数当做对象来调用时候执行__call__，像这样的对象叫做Callable对象。
callable(s)
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


## 枚举
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')) # 使用方式1
# 获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# member.value：访问的就是枚举对应的 0,1,2,3常量值。
## 如果想自己定义枚举中的值可以实现自己的类：
from enum import Enum, unique
@unique # 装饰器会检查保证没有重复的值
class Weekday(Enum): # 使用方式2
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


## type()
# 静态语言和动态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# type可以获取对象的类型，还可以动态的创建类。
# type可以获取类的类型
type(stu)
# type动态创建类
'''
要创建一个class对象，type()函数依次传入3个参数：
    1)class的名称；
    2)继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    3)class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
##通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
'''
def fn():
    pass
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class

# 元类（类模板）
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 先定义metaclass，就可以创建类，最后创建实例 ------(实例的创建过程)
## 用法
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
class ListMetaclass(type):# metaclass是类的模板，所以必须从`type`类型派生。
    def __new__(cls, name, bases, attrs):
        '''
        __new__()方法接收到的参数依次是：
        当前准备创建的类的对象；
        类的名字；
        类继承的父类集合；
        类的方法集合。
        '''
        attrs['add'] = lambda self, value: self.append(value) # 对其动态创建方法
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass): # 以类模板来创建类
    pass
## 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
## 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
### 作用示例：
#ORM：即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
# 也就是说我这个ORM框架只要给别人了,任何人都可以直接用于它的数据库映射,因为他是根据你传入的参数动态生成的类。一个框架使用全部！
