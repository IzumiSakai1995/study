# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 20:54:33
# @Author  : Izumi Sakai
# @File    : datetime_.py.py
# @Software: PyCharm
#获取当前时间
import time
from datetime import datetime     #datetime中的datetime类     import datetime.datetime
# now = datetime.now()
# # print(now)
# # print(type(now))
# # print(time.time())
# # print(now.timestamp())  #当前时间转换为时间戳

#时间戳转换当前时间
# now = time.time()
# print(datetime.fromtimestamp(now))

#str转换当前时间
# cday = datetime.strptime('2015-05-09','%Y-%m-%d')    #一个格式化时间
# print(cday)