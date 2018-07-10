#__author: Liu Zheng
#date:2018/6/21

#编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
        not self.count += 1

std1 = Student('bart')
print(Student.count)
print(std1.count)


