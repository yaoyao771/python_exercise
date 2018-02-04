#encoding:utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type : str
        :rtype: bool
        """
        parament = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:

            if c in parament.values():
                stack.append(c)
            elif len(stack) != 0:

                if c in parament.keys() and parament[c] == stack.pop():
                    continue
                else:
                    return False
            else:
                return False
        return len(stack) == 0