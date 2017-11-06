#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    @ author    zhaohaoren
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import functools
import unittest

'''
    目录：
        unittest模块
        setUp与tearDown
    简介：
    单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
    编写函数应该处理的用例，判断输入输出的结果是否正确，当对函数进行修改的时候，我们只要再次执行单元测试的用例
    如果函数的行为满足测试用例就能保证该模块依然正常！

'''
## unittest模块
# 自己的模块
class Dict(dict):
    pass
# 编写模块的测试用例
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b='test')
        # 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。
        # 最常用的断言就是assertEqual()：
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_keyerror(self):
        d = Dict()
        # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']
        # 访问不存在的key时，断言会抛出KeyError：
        with self.assertRaises(KeyError):
            value = d['empty']
#运行单元测试
# 1. 测试模块文件中加入下面代码 -> python3 test.py
if __name__ == '__main__':
    unittest.main()# 调用测试
# 2. python3 -m unittest test 加上-m unittest参数，推荐使用该方法！可以一次批量运行很多模块

## setUp()和tearDown()方法。
# 这两个方法会分别在每调用一个测试方法的前后分别被执行。你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码。
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')
    def tearDown(self):
        print('tearDown...')
