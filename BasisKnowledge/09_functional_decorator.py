#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：高阶函数 之 装饰器
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

'''
    @decorator,在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

    装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
    它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
    有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

    在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
    而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

    Python中一切皆对象: 函数，数据结构，类对象都是对象。
'''

#装饰器用于动态的增加一个函数的功能：

# 装饰器函数（给open_file增加些功能）
def log(open_file): # 必须传入被装饰的函数作为参数，@log作用就是将open_file传入该函数中
    print('Log：someone want to open a file')
    @functools.wraps(open_file)
    def wrapper(*args,**kwargs):
        open_file() # 在函数内部执行本来要调用的函数
    return wrapper # 必须返回一个函数，这个函数代表被装饰后的opne_file函数log的作用只是扩充函数功能

'''
    装饰器函数必须要点：
    1、@xxxx必须等于装饰器函数名称
    2、函数的参数必须是一个函数，用来接收被装饰函数
    3、函数的返回值必须是一个函数
    4、因为3中返回必须是一个函数，所以应该有个内部函数，这个内部函数中应当执行原函数内容，或者增加一些操作。

    装饰器函数的本质：传入需要被装饰的函数--> 增加所要的功能 --> 返回一个新的函数。
    它如果一个代理一样，程序执行原函数的时候，会移交给其代理执行！
'''

# 需要被装饰的函数 （此时我们需要在打开文件前输出一段log）
@log # 当发现有人调用open_file()时候，在@log处转为执行 log(open_file)
def open_file():
    print('file is opening!')

print(open_file.__name__)
open_file() # 调用这个时候 = log(open_file)


## 带参数的装饰器函数(装饰器本身就需要参数)
def log2(text): # 在外面再套一层函数
    # 也就是说以后我写代码需要啥已有功能的时候就不要自己全写了，只需要写主要内容然后装饰一下（如果有该装饰的话）
    def decorator(open_file):
        print('Log：'+text+' want to open a file2')
        @functools.wraps(open_file)  # 将返回的wrapper函数名字改为open_file2，需要加载wrapper上！
        def wrapper(*args, **kwargs):
            open_file()
        return wrapper
    return decorator


# 这个时候你把log('Justin')看出一个函数名
@log2('Justin')# 这样子去理解过程：先计算log('Justin')返回decorator函数，然后相当于@decorator
def open_file2():
    print('file2 is opening!')

print(open_file2.__name__)
open_file2() # = log('Justin')(open_file2)

