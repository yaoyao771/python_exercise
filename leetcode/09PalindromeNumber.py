#encoding:utf-8
def isPalindrome(x):

    a = 2 ** 31 - 1
    tmp=x
    y=0
    if x==0:
        return True
    if 0<x<a and x%10!=0:
        while 0<tmp<a:
            y=y*10+tmp%10
            tmp=int(tmp/10)
        if 0<y<a:
            print (y)
            return x==y

        else :
            return False
    else:
        return False

x=-12321
isPalindrome(x)
"""
    :type x: int
    :rtype: bool
 """
'''

    a = 2 ** 31 - 1
    tmp = x
    y = 0
    if x <= 0 or x / 10 == 0 or x==' ':
        return 0

    while tmp:
        y = y * 10 + tmp / 10
        tmp = tmp / 10
    if -a < x < a and -a < y < a:

        return y == x
    else:
        return 0
'''
