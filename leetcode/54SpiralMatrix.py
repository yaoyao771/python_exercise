'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.


'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        len_row = len(matrix)
        len_column = len(matrix[0])
        list_num = []
        count = min(len_row, len_column) / 2
        mod = min(len_row, len_column) % 2
        for i in range(0, count):
            a = len_row - i - 1
            b = len_column - i - 1
            for j in range(i, b):
                list_num.append(matrix[i][j])

            for j in range(i, a):
                list_num.append(matrix[j][b])
            for j in range(b, i, -1):
                list_num.append(matrix[a][j])
            for j in range(a, i, -1):
                list_num.append(matrix[j][i])
        if mod == 1:
            if len_row == len_column:
                list_num.append(matrix[count][count])
            elif len_row > len_column:
                for i in range(count, len_row - len_column + count + 1):
                    list_num.append(matrix[i][count])
            elif len_row < len_column:
                for i in range(count, len_column - len_row + count + 1):
                    list_num.append(matrix[count][i])
        return list_num


