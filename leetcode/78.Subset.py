
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [i+[num] for i in result]
        return result

'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.length=len(nums)
        times=self.length+1
        for i in range(times):
            self.dfs(nums,[],i,0)
        return self.res
    def dfs(self,nums,ans,k,start):
        if len(ans)==k:
            self.res.append(ans[:])
        for i in range(start,self.length):
            ans.append(nums[i])
            self.dfs(nums,ans,k,i+1)
            ans.pop()
        
'''
