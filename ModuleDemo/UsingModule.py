#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '   #第一行字符串默认是模块的文档注释

__author__ = 'Michael Liao'     #把作者变量写进去

#-------------------------------以上是Python的标准模板-----------------

import sys

print ('__name__ is',__name__)
def test():
    args = sys.argv #获取在命令行中的参数，第一个对应的.py名称
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 在当前模块下 执行会判断正确， 在其他地方导入该模块的话，判断失败test()不会执行的
# 就是说通过import ModuleTest的不会执行test()
if __name__=='__main__':        #如果是这个脚本被执行 __name__ = main,如果这个脚本是被import的，运行到这个的时候就不是main而是模块的名字
    test()

    # 每个模块都有一个内置的变量__name__
    #可以这么理解：
    # python file.py是直接执行脚本，相当于将file.py当成一个main函数，main里面有很多其他的方法。 这个时候__name__就是main
    # 如果是import file.py就相当于include一个文件，__name__就是文件名，
    #
    # 这也就是为什么 在文件内部直接执行test()。而import的module的话 只有 module.test()才会执行