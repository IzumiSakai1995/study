# -*- coding: utf-8 -*-
# @Time    : 2018/07/16 20:36:01
# @Author  : Izumi Sakai
# @File    : hashlib_module.py
# @Software: PyCharm

import hashlib  #加密

# # md5   唯一 不可逆
# md5 = hashlib.md5()
# print(md5)   #<md5 HASH object @ 0x0000000001DD2418>
# # <built-in function openssl_md5>
# # m.update('Hello World'.encode('utf8'))  python3中存的字符串为unicode
# md5.update('Hello World'.encode('utf8'))
# print(md5.hexdigest())  # b10a8db164e0754105b7a99be72e3fe5  十六进制
#
# md5.update('XiaoLiu'.encode('utf8'))   # 拼接起来的转换 Hello WorldXiaoLiu
# print(md5.hexdigest())  # 16ea8ba8af149838c796f3cce6fbc9bb
# 撞库 用简单字符加密拼接
# sha_demo = hashlib.sha256()    # 用得较多  算法比md5复杂
# sha_demo.update('hello world'.encode('utf8'))
# print(sha_demo.hexdigest())