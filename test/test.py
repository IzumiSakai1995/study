#__author: Liu Zheng
#date:2018/6/20

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s,%s' %(self.name,self.score))

bart = Student('lz',100)
Student.print_score(bart)