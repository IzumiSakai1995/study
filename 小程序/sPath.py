# author: Izumi Sakai
# date:2018/8/14 22:36

import os

def print_directory_contents(sPath):
    '''
    接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。
    :param sPath:
    :return:
    '''
    for childpath in os.listdir(sPath):
        childpath = os.path.join(sPath,childpath)
        if os.path.isdir(childpath):
            print_directory_contents(childpath)
        else:
            print(childpath)


print_directory_contents(r'd:\python')