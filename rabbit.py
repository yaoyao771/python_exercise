import numpy as np
'''

def rabbit(monnum):
    for i in range (0,monnum-2):
        num=[]
        num.append(2)
        num.append(4)

        num[i+2]=num[i]+num[i+1]


    print num
rabbit(5)

'''
''''''
def rabbit(monthnum):
    a=2
    b=4
    for i in range (3,monthnum+1):
        num=a+b
        a=b
        b=num
        rabnum = ([2, 4])
        rabnum.append(num)
    print rabnum
rabbit(5)










