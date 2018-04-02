'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        rindex = 0
        bindex = length
        i = 0
        j = length - 1
        while i <= j:
            if nums[i] == 0:
                rindex += 1
                i += 1
            elif nums[i] == 2:
                if nums[j] == 0:
                    rindex += 1
                    bindex -= 1
                    i += 1
                    j -= 1
                elif nums[j] == 2 and i != j:
                    bindex -= 2
                    i += 1
                    j -= 1
                elif nums[i] == 2 and i == j:
                    bindex -= 1
                    j -= 1
                else:
                    bindex -= 1
                    i += 1
            else:
                i += 1
        nums[:rindex] = [0] * rindex
        for i in range(rindex, bindex):
            nums[i] = 1
        for i in range(bindex, length):
            nums[i] = 2
