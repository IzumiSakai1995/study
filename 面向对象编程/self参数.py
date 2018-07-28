# author: Izumi Sakai
# date:2018/7/23

'''
# self 代表实例本身（调用方法的对象）
class Bar:
    def foo(self,arg):
        print(self,arg)


ex1 = Bar()
print(ex1)
ex1.foo(111)
'''

'''
class Bar:
    def foo(self,arg):
        print(self,self.name,self.age,self.gender,arg)


z = Bar()
z.name = 'Alex'
z.age = 18
z.gender = 'girl'
z.foo(111)
'''


# 构造方法

class Person:
    def __init__(self,name,age):
        '''
        构造方法
        __init__(self,arg):
            obj = ClassName('arg')
        创建对象时候自动执行
        做初始化
        '''
        self.n = name
        self.a = age

    def show(self):
        print('%s-%s' %(self.n,self.a))
z = Person('Alex',19)
z.show()
