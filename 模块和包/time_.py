# -*- coding: utf-8 -*-
# @Time    : 2018/07/15 23:25:36
# @Author  : Izumi Sakai
# @File    : time_.py
# @Software: PyCharm
import datetime
import time  # provides various functions to manipulate time values
# print(help(time))
# print(time.time())   输出时间戳  ****
# time.sleep(secs)      ******
# print(time.clock())  # 计算cpu执行时间
# print(time.gmtime())  # UTC 通用协调时  英国时间 time.struct_time(tm_year=2018, tm_mon=7, tm_mday=15, tm_hour=16,
# tm_min=26, tm_sec=48, tm_wday=6, tm_yday=196, tm_isdst=0 夏令时时间)
# print((time.localtime())) *****
# print(time.strftime('%Y %m %d %H %M %S')) *****  字符串时间
# print(time.strptime(time.strftime()))  转格式化时间
# a = time.strptime()
# a.tm_year
# print(time.ctime()) 格式定义好
# print(time.ctime(3600))
# print(time.mktime(time.localtime()))  #参数为tuple  结构化时间


# print(datetime.datetime.now())
print(datetime.datetime)