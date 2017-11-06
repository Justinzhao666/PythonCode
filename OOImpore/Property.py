#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates



#

class Screen(object):
    @property
    def width(self):  #将这个方法当成属性来使用，所以这个方法设置成变量的名字
        return self._width   #这个才是真正的类的属性
    @width.setter     #这个width是根据get的property来的，所以必须和property的函数一模一样！
    def width(self,width):  #同理：方法名必须和get的一样
        self._width = width

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height
    @property
    def resolution(self):
        return self._width * self._height

obj = Screen()
obj.height = 1024
obj.width =768
print(obj.resolution)
