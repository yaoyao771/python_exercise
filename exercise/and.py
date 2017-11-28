#encoding:utf-8
a = raw_input("输入一组数")
b = list(a)
n = len(b)
for i in range (n/2):
    b[i], b[n-1-i] = b[n-1-i], b[i]
print b