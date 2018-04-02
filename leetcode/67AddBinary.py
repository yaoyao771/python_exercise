'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


'''



class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        len_a = len(a)
        len_b = len(b)
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])
        if len_a >= len_b:
            a, b = b, a
        flag = 0

        for i in range(len_a - 1, len_a - len_b - 1, -1):
            a[i] = a[i] + b[i] + flag
            if a[i] > 1:
                flag = 1
                a[i] -= 2
            else:
                flag = 0
        for i in range(len_a - len_b - 1, -1, -1):
            a[i] += flag
            if a[i] > 1:
                flag = 1
                a[i] -= 2
            else:
                flag = 0

        if flag == 1:
            a.insert(0, 1)
        a_len = len(a)
        for i in range(a_len):
            a[i] = str(a[i])

        return ''.join(a)
