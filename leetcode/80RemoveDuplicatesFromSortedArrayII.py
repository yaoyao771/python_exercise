'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return length
        tmp = ''
        flag = 0
        i = 0
        while i < length:
            if nums[i] != tmp:
                flag = 0
                tmp = nums[i]
                i += 1
            elif nums[i] == tmp and flag == 0:
                flag = 1
                i += 1
            elif nums[i] == tmp and flag == 1:
                length -= 1
                nums.remove(nums[i])
        return len(nums)

