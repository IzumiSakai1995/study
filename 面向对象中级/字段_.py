# author: Izumi Sakai
# date:2018/7/2423:15

'''
类成员：
    字段：
        -普通字段 保存在对象中  只能通过对象访问
        -静态字段(static) 保存在类里面 能通过类和对象访问
    方法：
'''
class Foo:
    def __init__(self,name):
        '''普通字段'''
        self.name = name
        '''普通方法'''
    def show(self):
        print(self.name)


class Privince:
    country = '中国'    # 代码解释的时候创建
    def __init__(self,name):
        self.name = name


Henan = Privince('河南')
print(Privince.country)
