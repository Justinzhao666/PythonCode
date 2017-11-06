#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'


__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates
import unittest
from ExceptionDemo.mydict import Dict


class TestDict(unittest.TestCase):

    #在调用一个测试前后会 执行setup和setdown这两个方法：举例：连接数据库啊啥的
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
# 必须得是test为开头，不是test开头的不认为是测试方法。不被执行
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
# 两种断言方式：
# 第一种直接断言，推论出问题所在 self.assertEqual()
# 第二种断言是 抛出指定的类型的error with self.assertRaises()
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  #如果不存在key 断言抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
#可以直接以执行脚本方式执行测试，  也可以  -m unittest  UnitTestDemo方式执行测试
if __name__ == '__main__':
    unittest.main()
