#encoding:utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = sorted(nums)
        num_len = len(nums)
        result = a[0] + a[1] + a[num_len - 1]
        for i in range(0, num_len - 2):
            j, k = i + 1, num_len - 1

            while j < k:
                value = a[i] + a[j] + a[k]

                if value == target:
                    return value
                if abs(value - target) < abs(result - target):
                    result = value
                if value < target:

                    j += 1

                elif value > target:

                    k -= 1

        return result