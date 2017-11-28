#encoding:utf-8
class solution:


    def __iter__(self):
        return self
    def sum(self,l1,l2):
        sum=0
        list1=iter(l1)
        list2=iter(l2)
        listnum=[0]
        while 1:

            sum=next(list1)+next(list2)
            listnum.append(sum)

s=solution()
s.l1=(2,3,4)
s.l2=(4,5,2)
s.sum(s.l1,s.l2)

