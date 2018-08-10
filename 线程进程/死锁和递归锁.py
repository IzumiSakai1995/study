# author: Izumi Sakai
# date:2018/8/2 20:22

'''
RLock

'''
import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()
def doA():
    pass


class Account:
    def __init__(self,id,money):
        self.balance = money
        self.id = id
    def withdraw(self,num):
        self.balance -= num

    def repay(self,num):
        self.balance += num

def transer(_from,to,count):
    _from.wihtdraw(count)
    to.repay(count)

A1 = Account('Alex',1000)
A2 = Account('xiaohu',2000)

threading.Thread(target=transer())

