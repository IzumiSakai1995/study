#__author: Liu Zheng
#date:2018/6/21


class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s,%s' %(self.__name,self.__score))

    def set_score(self):
        self.__score = input('输入新的分数')

    def set_name(self):
        self.__name = input('输入新的姓名')

bart = Student('lz',100)
Student.print_score(bart)
Student.set_score(bart)
Student.print_score(bart)
