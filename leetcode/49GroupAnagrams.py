'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs = sorted(strs)
        ans = {}
        for s in strs:
            tmp = tuple(sorted(s))
            if tmp in ans:
                ans[tmp].append(s)
            else:
                ans[tmp] = [s]
        return list(ans.values())
