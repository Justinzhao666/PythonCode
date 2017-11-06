#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：高阶函数 之 闭包
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    python 中函数不仅可以当做变量，也可以当做返回值，这时候便有闭包的概念

    闭包是一种代码结构： 分为内部和外部（可以是类可以是方法），作为内部可以使用外部的所有变量

    注意：
    函数必须要()才能执行，没有()的时候只是代表一个函数的引用。f 只是一个引用，f()才是一个返回值！
    返回一个函数时，牢记该函数并未执行（想要立即执行肯定有 ref() 的语句），返回函数中不要引用任何可能会变化的变量。

'''

## 函数内部定义一个函数，使用内部的函数名用作返回值
def outer(things):
    def inner():  # 内部函数
        something = things # 内部函数引用外部变量
        return something
    return inner # 外部函数返回内部函数

## outer() 返回inner函数，但是不执行inner，只是返回一个函数的引用！
## 并且每次调用返回的函数名都不一样（每次调用outer返回的函数都是新的inner）
print(outer('something'))
f = outer('something')
## f只是函数的引用，执行函数必须加上"()"！
print(f())


## 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
## 即：内部函数不要引用外部会变化的量！
def count():
    fs = []
    for i in range(1, 4): # 内部函数f() 不要引用外部会变化的量！
        def f():
             return i*i
        fs.append(f)
    return fs
# 在执行f1 f2 f3的时候，他们的共同引用 i 都会变成4！！
f1, f2, f3 = count() # f1 = fs[0] f2 = fs[1] f3 = fs[2] 结果：
'''
    闭包保存着函数的运行状态，如果闭包中存在循环引用的话，所有的返回函数的状态其实都是指向那个循环引用！
    引用指向的值变化的时候，所有返回函数的引用值就都变了！
    代码角度讲：
        将代码拆开，fs = f(){i*i}（函数名指向的代码块） ,f(){i*i} ,f(){i*i}  这个i不会被立刻计算，最后i=4。 此时执行f()i是用4来计算的

    解决方法：
        在外部再套一层函数，将外部函数中每次return f的时候直接将结果计算出来后保存，这层函数就是用于保存返回函数的执行结果！
        def count():
            def f(j):
                def g():
                    return j*j
                return g
            fs = []
            for i in range(1, 4):
                fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()  这时候代码中g -> f(){1*1 (已经被计算)}
            return fs
        # 上述解决方法循环放到了f与g的外部，

    其实这样的结构也很少用！ 你看for循环都被提到了count中，和原来代码根本结构就不一致，关键点就在于f()
'''
