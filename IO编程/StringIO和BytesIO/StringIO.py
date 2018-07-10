# -*- coding: utf-8 -*-
#__author: Liu Zheng

#date:2018/6/21


from io import StringIO
# f = StringIO()
# f.write('hello')
# print(f.getvalue())

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO("Hello\nHi\nBye")
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())