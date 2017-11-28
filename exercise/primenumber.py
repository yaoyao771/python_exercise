from math import sqrt
def primenum():
    for i in range(101,201):
        flag=0

        for j in range(2,i):
            k=0
            if i%j==0:
                flag==1
                break
        if flag==0:
                k=k+1
                print(i)
    print (k)
primenum()