# -*- coding: utf-8 -*-
# @Time    : 2018/07/13 14:13:14
# @Author  : Izumi Sakai
# @File    : 列表生成式.py
# @Software: PyCharm
#运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁
# print(list(range(1,11)))
#循环
# L=[]
# for x in range(10):
#     L.append(x*x)
#
# print(L)
#列表生成式 将要生成的元素放在for前面，后面跟for循环 就可以把list创建出来
# L = [x * x for x in range(10)]
# print(L)

# print([x*x for x in range(10) if x%2 ==0])  仅偶数的平方
# print([m+n for m in "ABC" for n in "XYZ"]) #全排列

#使用两个变量来生成list
# dict_demo = {'a':'X','b':'Y','c':'Z'}
# L = [k + '=' + v for k,v in dict_demo.items()]
# print(L)
# #把list中所有字符串变小写
# print([s.lower() for s in L])
#
# L = ['Hello','World','Joe',23,164]
# print([s.lower() for s in L if isinstance(s,str)==True])