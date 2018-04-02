#encoding:utf-8


def permute( nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sub = []
        dfs(res,nums,sub)
        return res

def dfs(res, Nums, subList):
        if len(subList) == len(Nums):
            #print res,subList
            res.append(subList[:])
            print('d')
            print(subList)
        for m in Nums:
            if m in subList:
                continue
            subList.append(m)
            print('a')
            print(m)
            dfs(res,Nums,subList)
            print('b')
            print(subList)
            subList.remove(m)
            print('c')
            print(subList)
nums=[1,2,3]
permute(nums)