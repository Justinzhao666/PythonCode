#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Python 模块
    @ author    Justin Zhao
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools

'''
    在Python中，一个.py文件就称之为一个模块（Module）。
    模块间的间隔使用package包。
    模块中的变量定义表示的作用域
    第三方模块安装
'''

import  sys # 导入系统模块

def test():
    args = sys.argv # sys.argv 是python命令下的参数(list格式)，这里是[11_module.py,]
    print('---:'+args)

'''
    只有是执行当前模块才会执行下面的代码--->python 11_module.py : true
    如果是在其他模块中import这个模块，这里就不会执行-----> import 11_module.py : false

    作用：Make a script both importable and executable
    让一个脚本既可以导入，又可以自己执行！
    当你写的模块被import的时候，执行语句如果在最外围，那么其他模块在导入时候会执行你模块中的执行语句，
    这样就会对别人写的模块造成影响（没必要的输出）。加上main在其他模块导入的时候就不会执行main函数内容（importable），
    只有单独运行该模块的时候会执行main方法（executable），所以一个模块中最外围不应该有执行语句，
    但我们有时候要测试这个类，这时候测试的输出代码就应该放到main中，所以main中一般就是用于测试该模块，
    而我们import其他模块只是想用该模块的一些函数，这样做有效的保证了execute和import的隔离。
'''
if __name__ == '__main__':
    test() # 测试该模块的执行逻辑


## 变量命名规范:
# __xxx__ ： 特殊的变量
# __xxx,_xxx：private变量或者函数
# xxx：public变量或者函数
# 使用这些变量只是提示程序员该变量不应该被直接访问，Python并没有具体机制来阻止你访问，只是一种暗示！


# 安装第三方模块使用pip
# pip install Pillow
# python 查找模块会搜索当前目录、所有已安装的内置模块和第三方模块。路径都放在sys.path中
# sys.path.append('/Users/michael/my_py_scripts') 也可以直接添加搜索的路径或者设置环境变量。