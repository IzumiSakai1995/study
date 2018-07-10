#__author: Liu Zheng
#date:2018/6/24

from multiprocessing import Process
import os

#子进程执行的代码：
def run_proc(name):
    print('Run child processing %s (%s)' %(name ,os.getpid()))

if __name__=='__main__':
    print('Parent progress %d' % (os.getpid()))
    p  = Process(target=run_proc,args=('test'))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')