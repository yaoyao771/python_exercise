#encoding:utf-8
import numpy as np
def solution(nums):
    '''
    a=sotred(nums)
    len_num=len(nums)
    num_list=[]
    i=0
    while i<=a.index(0):
        nums=a.count(a[i])
        j,k=i+1,len_num-1
        print(i,j,k)
        while j<k:
            if a[i]+a[j]+a[k]<0 and j<k-1:
                j+=1

            if a[i]+a[j]+a[k]>0 and j<k-1:
                k-=1


            if a[i]+a[j]+a[k]==0:
                b=[a[i],a[j],a[k]]
                num_list.append((b))
                m=a.count(a[j])
                n=a.count(a[k])

                j+=m-1
                k-=n
            else:
                break



        i+=nums
    '''
    a = sorted(nums)
    len_num = len(nums)
    num_list = []
    i = 0
    while i < len_num - 2:

        j, k = i + 1, len_num - 1
        while j < k:
            if a[i] + a[j] + a[k] < 0 and j < k - 1:
                j += 1
            if a[i] + a[j] + a[k] > 0 and j < k - 1:
                k -= 1
            if a[i] + a[j] + a[k] == 0:
                b = [a[i], a[j], a[k]]
                if b not in num_list:
                    num_list.append((b))
                    i+=1



                else:
                    i += 1
            else:
                i+=1

    return num_list

    print(num_list)
num=[-1,0,1,2,-1,-4]
solution(num)




