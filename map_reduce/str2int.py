from functools import reduce
DIGITS  = {'0':'0','1':'1','2':'2'}
def str2int(s):
    def fn(x,y):
        return x*10 +y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
