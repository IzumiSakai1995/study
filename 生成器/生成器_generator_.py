# -*- coding: utf-8 -*-
# @Time    : 2018/07/13 15:41:58
# @Author  : Izumi Sakai
# @File    : 生成器_generator_.py
# @Software: PyCharm

g = (x*x for x in range(10))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  错误示范

# for n in g:
#     print(n)  基本使用for 循环对生成器进行迭代
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n=n+1
        print(n)

fib(6)


