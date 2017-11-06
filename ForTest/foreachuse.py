#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    @ author    zhaohaoren
    @ date
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script
import random

'''
    目录：

    简介：

'''


nums = range(1, 10)
for num in nums:
    nums = range(11, 14)
    print(num)



def cal():
    number = random.randint(1, 20);
    return number;

def loop(a):
    for num in range(1,a):
        new_a = cal();
        loop(a)
