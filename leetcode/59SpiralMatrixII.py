class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        count = n / 2
        index = n % 2
        matrix = [[0] * n] * n
        nums = 1
        for i in range(0,count):
            length = n - i - 1
            a = i
            for j in range(i, length):
                matrix[i][j] = nums
                nums += 1
            for j in range(i, length):
                matrix[j][length] = nums
                nums += 1
            for j in range(length, i, -1):
                matrix[length][j] = nums
                nums += 1
            for j in range(length, i, -1):
                matrix[j][i] = nums
                nums += 1

        if index == 1:
            matrix[count][count] = nums
        return matrix

