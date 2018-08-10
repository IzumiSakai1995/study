# author: Izumi Sakai
# date:2018/7/29 21:16

'''
IO密集型 阻塞
计算密集型
GIL 在同一时刻只能有一个线程进入解释器
'''
import threading
import time

beg = time.time()
def foo():
    print('ok')
    time.sleep(1)
def bar():
    print('ok2')
    time.sleep(2)

t1 = threading.Thread(target=foo())

t2 = threading.Thread(target=bar())

t1.start()
t2.start()

end = time.time()
print(end-beg)