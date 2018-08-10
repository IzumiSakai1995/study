# author: Izumi Sakai
# date:2018/8/2 21:17

import threading
'''
条件变量(condition)
进程间通信
wait()  ：条件不满足时调用，线程释放锁并进入等待阻塞
notify()： 条件创造后调用，通知等待池激活一个线程
notifyAll()： 条件创造后调用，通知等待池激活所有线程
'''

lock_con = threading.Condition()
