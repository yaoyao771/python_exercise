def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0 or n == 1:
        return len(nums)

    j = 0
    i = 1
    while i < len(nums) - 1:
        if nums[i] != nums[j]:
            j += 1

        else:
            nums[j] = nums[i]

        return j + 1
