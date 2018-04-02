'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.


'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        length = 0
        if s == '':
            return 0
        while s[n - 1] == ' ' and n > 0:
            n -= 1
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1
        return length
