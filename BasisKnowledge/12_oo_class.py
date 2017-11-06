#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 面向对象 类
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

'''
    类的定义形式
    创建对象方式
    构造函数
    this 在Python中是self
    成员属性：设置 private，public
    继承，多态
    静态语言 vs 动态语言，鸭子类型
    type(),isinstance(),dir()
'''

class MyClass(object):
    attr = 'hello' # 类本身的成员属性，所有的该类对象都拥有！
    # 相当于构造函数，第一个参数永远是self，表示实例本身。__init__是特殊的！
    def __init__(self,attr1,attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        self.__attr3 = 'private' #前面加上两个下划线的变量是private的，外部无法直接访问
        self.__special__ = 'special' # __xx__ 是特殊变量，可以被外部访问
        self._attr4 = 'half-private' #虽然我可以外部被访问，但是，请把我视为私有变量，不要随意访问
    # 普通成员函数的定义
    def getAttr1(self):
        return self.attr1

mm = MyClass('zhao','haoren')

mm.newAttr = 'hello' # python运行直接定义其成员属性，不需要在内部申请！这是Python动态语言的特性，但是这个属性只属于该对象！
def f1():
    pass
mm.newFun = f1 # 对于函数也同样适用，但是这些属性和方法只属于该对象！

print(mm.attr1)
print(mm.getAttr1())

# Python中的继承
class SubClass(MyClass):
    pass

# 多态
# mm = SubClass() #父类被子类初始化
## 动态语言和静态语言
# 静态语言要求父类被传入的只能是其本类或者子类的对象；但是动态语言只需要有一个run方法就可以了！
# 鸭子类型：它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

# type
type(124) == type(3) # true，type函数返回对应的class类型。
print(type(mm))
import types # 判断对象是否为一个函数
def fn():
    pass
type(fn)==types.FunctionType #/types.BuiltinFunctionType/types.LambdaType/types.GeneratorType
# isintance 判断已知类型
# dir 获得一个对象的所有属性和方法，返回一个字符串的list
print(dir(mm))

'''
    tips:
    #为什么要设置一个函数来获取一个变量：
        可以对用户的参数做检查，不会导致的传入错误的数据！
    #不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
    所以，仍然可以通过_Student__name来访问__name变量：
'''
