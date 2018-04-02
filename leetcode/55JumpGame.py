'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.


'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length == 0:
            return False
        index = nums[0]
        for i in range(1, length):
            if index < i:
                return False
            index = max(index, nums[i] + i)
            if index >= length - 1:
                return True
        return index >= length - 1

