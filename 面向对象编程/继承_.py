# author: Izumi Sakai
# date:2018/7/2322:48
'''
面向对象：继承
class GrandFather:
    pass

class Father(GrandFather): # 父类  基类
    pass

class Son(Father): # 子类  派生类  继承所有父类方法   调用方法时从子类开始往父类向上寻找   不影响self（永远指代调用
方法的对象）
    pass
'''

class Father:
    def f1(self):
        print('f1')

    def f2(self):
        print('f2')

class Son(Father):
    def s1(self):
        print('s1')

    def s2(self):
        print('s2')

    # def f2(self):
    #     super(Son, self).f2()   # 执行父类中的f2方法  super(ClassName, self).method()
    #     print('s.f2')
    def f2(self):
        F.f2(self)   # 将obj传入父类中的f2方法

s = Son()
s.f2()
'''
# 多继承   寻找方法时 从左到右 遍历查找  默认遍历完一支再遍历另外一支
# 如果有共同的根 不寻找根 遍历其他父类 都没有的时候找根
a.左侧优先
b.一条线遍历完
c.同一个根时，根最后运行
'''
class F0:
    def f1(self):
        print('f0')

class F1:
    def f1(self):
        print('f1')

class F2:
    def f1(self):
        print('f2')

class S1(F1,F2):
    pass
