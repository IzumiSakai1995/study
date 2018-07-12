# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 15:05:30
# @Author  : Izumi Sakai
# @File    : 递归函数.py
# @Software: PyCharm

#recursive function 递归函数
#用递归函数写阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(10))

#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
#递归能做的  循环都能做  递归效率低