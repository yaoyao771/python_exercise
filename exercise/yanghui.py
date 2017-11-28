#coding:utf-8
a = s = [1]
for i in range(0,10):
    for j in range(i+1):
        if j == 0 or i == j:
            s.append(1)
            print 1,
        else:
            s.append(a[j]+a[j-1])
            print a[j]+a[j-1],
    print
    a,s=s,[]
