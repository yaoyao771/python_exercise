'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxsum = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            max_sum = max(nums[i], nums[i] + max_sum)
            maxsum = max(maxsum, max_sum)
        return maxsum
