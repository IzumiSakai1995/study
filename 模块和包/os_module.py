# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 14:12:58
# @Author  : Izumi Sakai
# @File    : os_module.py
# @Software: PyCharm
# os 操作系统
import os
# print(os.getcwd())
# print(help(os))
# os.chdir('dirpath') #改变工作目录
# os.curdir()   #.   返回当前目录
# # os.pardir()  # 获取父目录
# # os.makedirs(r'abc\alex')    # 生成多个文件夹
# os.mkdir()  #生成文件夹
# os.removedirs(r'abc\alex')   # 删除多个空文件夹  r表示原生字符串  不进行转义
# os.rmdir()  #删除一个空文件夹
# print(os.listdir())
# print(os.linesep) 换行
# print(os.pathsep)    打印路劲分隔符  win下为; ,linux下为:
# print(os.name)
# print(os.system('dir'))  #执行shell命令
# print(os.environ)
# print(os.path.abspath('path'))  #返回绝对路径
# print(os.pathsep.split())    # 对当前路径进行分割   返回元组形式路径+文件名
# print(os.path.dirname('dir'))    # 取文件夹所在文件夹的名字  需要路径（相对或者绝对）
# print(os.path.dirname(__file__))   # 模块调用
# print(os.path.basename())   #返回path 最后的文件名
# os.path.exists()   #存在返回True 不存在返回False
# os.path.isabs()   #判断是否绝对路径
# os.path.isfile()   #判断是否存在
# os.path.isdir()   #判断是不是文件夹
# os.path.join()   #路径拼接
# os.path.getatime()  #最后存取时间
# os.path.getmtime() #最后修改时间
