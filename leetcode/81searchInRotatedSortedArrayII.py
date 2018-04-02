'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.


'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        lindex = 0
        rindex = length - 1
        mid = lindex + (rindex - lindex) / 2
        while lindex <= rindex:
            if nums[mid] == target or nums[lindex] == target or nums[rindex] == target:
                return True
            if nums[lindex] < nums[mid]:
                if nums[lindex] < target < nums[mid]:
                    rindex = mid - 1
                    mid = lindex + (rindex - lindex) / 2
                else:
                    lindex = mid + 1
                    mid = lindex + (rindex - lindex) / 2
            elif nums[lindex] > nums[mid]:
                if nums[mid] < target < nums[rindex]:
                    lindex = mid + 1
                    mid = lindex + (rindex - lindex) / 2
                else:
                    rindex = mid - 1
                    mid = lindex + (rindex - lindex) / 2
            elif nums[lindex] == nums[mid]:
                lindex += 1
                rindex -= 1

        return False
