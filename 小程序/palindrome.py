# author: Izumi Sakai
# date:2018/8/16 12:31
# 判断字符串是否是回文,使用递归的方式


def isPalindrome(s):
    if len(s) < 2:
        return True

    elif s[0] != s[-1]:   # 检查第一项和最后一项是否等同
        return False
    return isPalindrome(s[1:-1]) # 第一项等于最后一项，去除后返回

str = input('>>>请输入一个字符串')
if isPalindrome(str):
    print(str+'是一个回文字符串')
else:
    print(str+'不是一个回文字符串')

