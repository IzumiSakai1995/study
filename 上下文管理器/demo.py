# -*- coding: utf-8 -*-
# @Time    : 2018/07/14 16:55:45
# @Author  : Izumi Sakai
# @File    : demo.py
# @Software: PyCharm

# 基本用法
# with <expression>:
#     <block>
# <expression>执行的结果返回了一个实现上下文管理器的对象，即实现了这两个方法：__enter__ 和__exit__
with open('myfile.txt','w') as f:
    # do something for f
    f.write('hello world')

