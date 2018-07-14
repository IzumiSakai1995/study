# -*- coding: utf-8 -*-
# @Time    : 2018/07/14 16:25:44
# @Author  : Izumi Sakai
# @File    : try_except.py
# @Software: PyCharm
import math
while True:
    try:
        text = input('>')
        if text == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print('log10({0}) = {1}'.format(x, y))
    # except ValueError:
    #     print('The value must be bigger than 0')
    except Exception:    # 捕获所有异常
        print('The value must be bigger than 0')


