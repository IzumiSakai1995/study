#__author: Liu Zheng
#date:2018/6/21


#fpath = 'r'D:\python\study\IO编程\文件读写\text''

#读取模式
f = open('text','r')
f.readline()#按行读取  第一行
f.readline()#第二行 内部指针位移
f.readlines()#输出列表 将每个readline输出最后内容放入列表并输出
for i in f.readlines():
    print(i.strip())


##写入模式
#      open('test','w') 创建写模式对象时清空原文件所有内容
# f = open('text','w')
# f.write('lz\n')
# f.write('lyy')
# f.close()

###追加模式
# f = open('text','a')#追加模式
# f.write()
# f.close()
#
# dic = str({'1':'1111'})  #将字典写入文件
# f = open('test.txt','w')
# f.write(dic)
# f.close()

f = open('test.txt','r')
data = f.read()
print(eval(data)['1'])   #先eval 再[]
