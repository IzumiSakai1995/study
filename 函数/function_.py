# -*- coding: utf-8 -*-
# @Time    : 2018/07/14 15:24:35
# @Author  : Izumi Sakai
# @File    : function_.py
# @Software: PyCharm
"""
函数 function
Python中函数是一种基本类型对象，意味着：
可以将函数作为字典的储存
可以将函数作为参数传递给另一个函数
可以作为返回值
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
# -------------------------------------
# 函数进阶
# 作为字典的值
# def square(x):
#     return x**x
#
#
# def cube(x):
#     return x**x**x
#
#
# funcs = {
#     'square':square,
#     'cube':cube
# }
# x = 2
# for func in funcs:
#     print(func, funcs[func](x))
'''
Python 中函数传递方式是call by reference 即引用传递，
x = [10,11,12]
传递给 f 的是一个指向 x 的引用，如果我们修改了这个引用所指向内容的值（x[0]=999）
如果在函数中赋值给 x 一个新的值，那么函数外面的 x 的值不变
'''
# x = [1,2,3]
# def mod_f(x): # 修改引用所指向内容的值
#     x[0] = 999
#     print(x)
# print(x)
# mod_f(x)
# print(x)

# x = [1,2,3]    # 赋一个新值
# def demo_f(x):
#     x = [4,5,6]
#     return x
# print(x)
# print(demo_f(x))
# print(x)

# x = 1
# def print_x():
#     global x
#     x = 10
#     print(x)
#
#
# print_x()
# print(x)
import time
