'''
filter求素数
埃式筛法
'''

# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x%n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter() #初始序列
#     while True:
#         n = next(it) #返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n),it)
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
def func_demo(s):
    if s != 'a':
        return s

str_demo = ['a','b','c','d','e']
ret = filter(func_demo,str_demo,) #参数：函数，序列
print(list((ret)))