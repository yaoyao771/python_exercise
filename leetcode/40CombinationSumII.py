class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.list = []
        self.length = len(candidates)
        flag = [0] * self.length
        self.combinationSum_2(candidates, target, [], 0, flag)
        return self.list

    def combinationSum_2(self, candidates, target, sublist, last, flag):
        if target == 0:
            self.list.append(sublist[:])
        if target < candidates[0]:
            return
        l = None
        for m in range(self.length):
            n = candidates[m]
            if n > target:
                return
            if n < last or l == n or flag[m] == 1:
                continue
            sublist.append(n)
            flag[m] = 1
            self.combinationSum_2(candidates, target - n, sublist, n, flag)
            flag[m] = 0
            l = n
            sublist.pop()
