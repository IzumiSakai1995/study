# -*- coding: utf-8 -*-
# @Time    : 2018/07/12 19:28:21
# @Author  : Izumi Sakai
# @File    : for_.py
# @Software: PyCharm
# for :python中语句依据任意序列中的子项，按它们在序列中的顺序来进行迭代

'''
collatz 猜想:小于7*10^11的自然数经过若干次变换后必然会到纯偶数4^n：16-8-4-2-1的循环
如果是个奇数 变换为3N+1
如果是个偶数 变化为N/2
最终得到1
example : 7-->22-->11-->34-->17-->52-->26-->13-->40-->20-->10-->5-->16-->8-->4-->2-->1
打印出每一步的结果
并打印出总变换次数
'''


def collatz(n):
    sequence = []
    global time
    time = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3+1
        time += 1
        sequence.append(n)
    return sequence


def main():
    for x in collatz(27):
        print(x)


if __name__ == '__main__':
    main()
    print('Time=', time)

import re

