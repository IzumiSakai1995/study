# author: Izumi Sakai
# date:2018/8/1 18:28

import threading
def addNum():
    global num
    num = 100

r = threading.Lock()

thread_list=[]

r.acquire()

r.release()