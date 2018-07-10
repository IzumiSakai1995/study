#__author: Liu Zheng
#date:2018/6/24


import json
d = dict(name = 'lz',age = 22,score = 99)
'''
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：'''
print(json.dumps(d))
print(d)
