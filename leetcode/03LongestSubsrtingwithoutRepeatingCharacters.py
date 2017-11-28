#encoding;utf-8
import math
class solution:
    def lengthoflongestsubstring(self,s):
        s=list(s)
        n1=0
        n2=0
        idex=0
        if len(s)==1:
            n1=1
        else:
            for i in range(1,len(s)):
                for j in range(idex,i):
                    if s[j]==s[i]:
                        idex+=1

                    n2=i-idex
                    n1=max(n1,n2)

        print (n1,n2,idex,len(s))


if __name__=='__main__':
    so=solution()
    so.s='abdeddpo'
    so.lengthoflongestsubstring(so.s)

    


