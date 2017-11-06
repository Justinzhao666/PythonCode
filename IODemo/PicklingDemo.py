#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

import pickle

d = dict(name = 'Bob',age = 20,score = 100)
print(pickle.dumps(d)) #将对象序列化为bytes


import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):  #json 有个默认参数决定怎么转换为json数据  --键值对形式
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
json.dumps(s,default=student2dict) #student2dict 就是转换的方式
json.dumps(s,default=lambda obj: obj.__dict__) #方法2 利用自带属性__dict__它的返回值就是一个dict包含对象的变量


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
#将json数据转换为对象 也要传入一个dict2student对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

