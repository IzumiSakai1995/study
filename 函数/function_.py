# -*- coding: utf-8 -*-
# @Time    : 2018/07/14 15:24:35
# @Author  : Izumi Sakai
# @File    : function_.py
# @Software: PyCharm
"""
函数 function
"""
# def fn_add(x,y):
#     return x+y
#
# print(fn_add(1,2))
#
# print(fn_add('Hello','World'))

# 带默认参数的函数


# def fn_add(x, y=10, z=0):
#     return x+y+z
#
#
# print(fn_add(1, 2, 3))
# print(fn_add(1, y=3, z=3))
# print(fn_add(1))

# 接收不定参数
# def add(x, *args):     #不能使用关键词传入参数
#     total = x
#     for arg in args:
#         total += arg
#     return total
#
#
# print(add(1, 2, 3, 4, 5, 6))

# def add(x, **args):
#     total = x
#     for arg, value in args.items():
#         total += value
#     return total
#
#
# print(add(1, a=2, y=3, z=4))

# 返回多个值
# from math import atan2
# def to_polar(x, y):
#     r = (x**2 + y**2) ** 0.5
#     theta = atan2(x, y)
#     return r, theta


# ret = to_polar(3, 4)
# print(type(ret))   # 函数将返回的多个值变成元组
# print(ret)
# r, theta = to_polar(3, 4)
# print(r, theta)    # 对两个变量赋值

# 将参数以元组形式传入
# tuple_demo = (3, 4)
# ret = to_polar(*tuple_demo)
# print(ret)

# 通过字典传入参数
# dict_demo = {'x': 3, 'y': 4}
# print(to_polar(**dict_demo))
