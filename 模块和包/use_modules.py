# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 22:09:42
# @Author  : Izumi Sakai
# @File    : use_modules.py
# @Software: PyCharm


# 模块用来组织函数
# python标准库
# 第三方模块
# 程序自定义模块  .py文件
# import sys
# from module_test.test_demo import add
# # 搜索路径： sys.path   # 解释器通过搜索类型找到模块文件之后解释.py文件中的所有代码
# print(add(1,2))
# print(sys.path)

# from module_test.test_demo import *   #引用覆盖问题 尽量少用
# print(add(1,2))
#
# form module_test.test_demo import add as new_name # 新定义导入函数名字