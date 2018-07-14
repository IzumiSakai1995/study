#__author: Liu Zheng
#date:2018/6/24


# import json
# d = dict(name = 'lz',age = 22,score = 99)
'''
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
Json表示出来是一个字符串，可以被所有语言读取，方便地存储到磁盘，可以再web页面中读取
要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：'''
print(json.dumps(d))
print(d)
