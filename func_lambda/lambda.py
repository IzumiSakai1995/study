from functools import reduce
def char2num(s):
    return DIGIT[s]

def str2int(s):
    return reduce(lambda x,y:x*10 + y,map(char2num,s))
