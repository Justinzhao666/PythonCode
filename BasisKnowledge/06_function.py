#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 中的函数
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    将函数当做参数的函数称为高阶函数。

    可以使用默认参数、可变参数和关键字参数
    默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
    *args是可变参数，args接收的是一个tuple（*）；
    **kw是关键字参数，kw接收的是一个dict（**）。
    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
'''
#----------------------------- 函数 -----------------------------------#
# 定义一个函数
def function(x):
    # 要记得参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 调用一个函数
function(1)

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
fact(1000)
# 当递归的太深的时候会栈溢出！解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#----------------------------- 返回值 -----------------------------------#
# 函数返回多个值
def returnMutliValue():
    '''
    :return: 其实是一种假象，返回的是一个返回值组成的tuple
    '''
    return 1,2,3


#----------------------------- 参数 -----------------------------------#
# >默认参数
# 应该和c一样默认参数必须在最后面定义，不然会有二义性
## 定义默认参数要牢记一点：默认参数必须指向不变对象！
def defParmas(x, n=2):
    pass

# >可变参数：为了tuple或list型参数
# 允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 使用 '*' 号，将参数转为一个tuple，所以意义不大，不确定要多少参数的话就指定一个list或者tuple参数传入就行了
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 使用方法1：直接传入任意参数
calc(1,2,3) #将1,2,3转为一个tuple传入
# 使用方法2：将一个list传入参数，用*
nums = [1,2,3]
calc(*nums) # 可以直接将一个list或者tuple使用*可以将其转为可变元素传入函数（很常见）

# >关键字参数：为了dict型参数
# 允许你传入0个或任意个 含参数名 的参数，这些关键字参数在函数内部自动组装为一个dict
# 关键字参数**就是可以传入 key=value这样的参数，用于接受字典类型参数
def person(**kw):
    print( 'other:', kw)
# 使用方法1：直接传入带参数名的参数-值对
person(gender='M', job='Engineer') # = name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
# 使用方法2：传入dict，用**
extra = {'city': 'Beijing', 'job': 'Engineer'}
person(**extra)

# >命名关键字参数
# 针对关键字参数的key设置限制，只允许传入指定key的key=value参数
def person(name, age, *, city='beijing', job): # * 之后接上 对关键字key的限制，限制key可以带默认参数
    print(name, age, city, job)

# >组合参数
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
## 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw): # *args只接受tuple/list的数据，kw只接受dict数据
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2, 3, 'a', 'b', x=99)
# >a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # 任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。*args, **kw代表了所有可以接受的数据类型
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}