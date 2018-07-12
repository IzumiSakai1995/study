# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 15:31:01
# @Author  : Izumi Sakai
# @File    : 装饰器函数.py
# @Software: PyCharm

#作用域：
#闭包：
def outer():  #外部函数
    x = 10
    def inner():
        print(x)  #内部函数中引用到了外部函数的临时变量
    return inner   #返回值是内函数的引用

f = outer()
f()
#在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
#装饰器：扩展原来函数功能的函数,
# def decorator_demo():
#     print('ok')
# @decorator_demo()
# def demo():
#     print("Hello world")
#
#
# print(demo.__name__)
