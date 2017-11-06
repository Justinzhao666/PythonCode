#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 高级特性：生成器
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

'''
    # 列表生成式是生成一个list，这个list是会受到内存的限制，列表的容量是有限的。@see: BasisKnowledge/07_feature_list_comprehensions.py
    # 生成器是一个动态的数据生成过程，数据在不断循环中推算出后续的元素。这种一边循环一边计算的机制，称为生成器：generator。
    # 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

    可以将list comprehensions简单的改为generator [] -> ()

    ## list_comprehensions ： 保存的是数据
    ## generator : 保存的是算法,以及计算的状态
    ## generator也是可迭代对象，可以用for
'''

# 创建一个generator， 将列表生成式的[]变为()
g = (x * x for x in range(10)) # generator不会将内部的for全部运算出来，而是保存状态和算法，在下一次需要取值的时候计算出值
# 不断的用生成式生成数据（不常用）：迭代到没有迭代东西时候会报出：StopIteration错误
next(g)
# 使用for来取出元素 （常用）: for的过程其实就自动调用next(g)然后赋值给n
for n in g:
    print(n)

# 函数generator @关键：yield
# 例如斐波那契数列，和生成器使用条件和相似：有规则，需要动态生成
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b ## a = (b,a+b)[0] ; b = (b,a+b)[1]
        n = n + 1
    return 'done'
'''
    ## generator和函数的执行流程不一样:
        ## 普通函数：顺序执行，遇到return就返回。
        ## generator函数：每次调用next的时候执行，遇到yield的时候中断返回yield的值，再次调用next的时候继续上次的中断执行
        迭代器无法获得函数中return的值，只可以获得yield的值。如果想要获得return的值需要用异常处理方式。

        def odd():
            print('step 1')
            yield 1
            print('step 2')
            yield(3)
            print('step 3')
            yield(5)
        next(odd) = 1
        next(odd) = 2
        next(odd) = 3
        next(odd) = StopIteration
'''



