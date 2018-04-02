class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1, l2 = len(num1), len(num2)
        list_num = [0] * (l1 + l2 - 1)
        if int(num1) == 0 or int(num2) == 0:
            return str(0)
        for i in range(l1):
            for j in range(l2):
                list_num[i + j] += int(num1[i]) * int(num2[j])
        flag = 0
        for i in range(l1 + l2 - 1):
            list_num[i] += flag
            list_num[i], flag = list_num[i] % 10, list_num[i] / 10

        if flag > 0:
            list_num.append(flag)
        list_num = list_num[::-1]
        return ''.join([str(x) for x in list_num[:]])
