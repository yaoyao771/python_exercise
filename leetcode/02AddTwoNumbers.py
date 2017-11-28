#encoding:utf-8
class solution():
    def addTwonumbers(self,l1,l2):
        n1=len(l1)
        n2=len(l2)
        a = 0
        b=0
        sum=0
        while n1!=0 and n2!=0:
            for i in range(n1):
                a+=l1[i]*(10**(n1-i-1))
            for j in range(n2):
                b+=l2[j]*(10**j)
            sum=a+b
            print (sum)
            break

if __name__=='__main__':
    s=solution()
    s.l1=[2,4,3]
    s.l2=[5,6,4]
    s.addTwonumbers(s.l1,s.l2)


