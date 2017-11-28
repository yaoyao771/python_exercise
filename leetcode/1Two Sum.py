#encoding:utf-8
#encoding:utf-8
class solution:
    def varies(self,target,nums):
        self.target=target
        self.nums=nums
    def twosum(self,target,nums):
        n=len(nums)
        for i in range(n-1):
            for j in range(i,n):
                if nums[i]+nums[j]==target:
                    print (nums[i],nums[j])
        return (i,j)
if __name__=='__main__':

    s=solution()
    s.nums=[2,7,9,11]
    s.target=9
    s.twosum(s.target,s.nums)
