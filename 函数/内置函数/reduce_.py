# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 16:02:45
# @Author  : Izumi Sakai
# @File    : reduce_.py
# @Software: PyCharm

from functools import reduce

def add(x,y):
    return x+y

print(reduce(add,range(1,10))) #叠加