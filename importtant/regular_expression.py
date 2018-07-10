#__author: Liu Zheng
#date:2018/6/29


import re

str = 'hello 12314123 &U&(*^*%*^*&#@!&%(*&!(ADSA This is a re demo'

#泛匹配
resoult = re.match('^hello.*demo$',str)
print((resoult))


