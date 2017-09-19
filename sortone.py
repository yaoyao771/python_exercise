#encoding:utf-8
a = [2, 3, 5, 7, 9, 23, 56]
n = len(a)
b = input("输入")
for i in range(n):

    if a[i] < b < a[i+1]:
        a.insert(i+1, b)
        break

    elif b > a[n-1]:
        a.append(b)
        break

print a
