# -*- coding: utf-8 -*-
# @Time    : 2018/07/15 23:01:21
# @Author  : Izumi Sakai
# @File    : 迭代器.py
# @Software: PyCharm
# 生成器都是迭代器 迭代器不一定是生成器
# 迭代器：1. 有iter方法 2.有next方法   （迭代器协议
# 可迭代对象 list tuple string :Iterable  不具有next方法
L = [1,2,3,5]
# print(L.__iter__()) =
d = iter(L)   # iter 方法返回了一个迭代器(Iterator)对象
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# for 循环内部三件事
# 调用可迭代对象的iter方法，返回一个迭代器对象
# 不断调用迭代器的next方法
# try...except 处理StioIteration异常
# for i in [1,2,3,4]:

# from collections import Iterator
# print(isinstance(d, Iterator))

