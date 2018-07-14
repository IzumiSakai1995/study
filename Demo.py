# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 14:54:54
# @Author  : Izumi Sakai
# @File    : Demo.py
# @Software: PyCharm

def fact(n):
    if n  ==1 :
        return 1
    return n*fact(n-1)

print(fact(10))