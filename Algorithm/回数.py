#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    this file is work for ? ---- edit with yours
    @ author    Justin Zhao
    @ date      2018/1/1
    @ version   1.0
"""

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates -> Python Script

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(1221))
print(is_palindrome(123))