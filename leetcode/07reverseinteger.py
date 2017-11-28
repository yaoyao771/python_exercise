#encoding:utf-8
import operator

def reverse( x):
        """
        :type x: int
        :rtype: int
        """
'''
        x_min=-2**30
        x_max=2*21-1
        a=list(str(abs(x)))
        s=int(x/abs(x))
        if x/10==0:
            b=a[len(a)-1::-1]
        else:
            b=a[len(a)::-1]
        k=int("".join(b))
        d=s*k
        if x_min<x<x_max and x_min<d<x_max:

               return d
        else:
                return -1
'''



def reverse( x):
        """
        :type x: int
        :rtype: int
        """
        x_min = -2 ** 31+1
        x_max = 2 ** 31 - 1
        if x != 0:
                a = list(str(abs(x)))
                s = int(x / abs(x))
                if x / 10 == 0:
                        b = a[len(a) - 1::-1]
                else:
                        b = a[len(a)::-1]
                k = int("".join(b))
                d = s * k

                if x_min<x<x_max and x_min<d<x_max:
                        print(d)



        else:
                return 0
x = -120
reverse(x)
print (2**31)
