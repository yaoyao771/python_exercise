'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix)
        if row == 0:
            return False
        column_len = len(matrix[0])
        if column_len == 0:
            return False
        column = column_len - 1
        start = 0
        end = row - 1
        while start <= end:
            mid = start + (end - start) / 2
            if target == matrix[mid][0] or target == matrix[mid][column]:
                return True
            if matrix[mid][0] < target and matrix[mid][column] > target:
                break
            if target < matrix[mid][0]:
                end = mid - 1

            else:
                start = mid + 1
        if start <= end:
            lcolumn = 0
            rcolumn = column

            while lcolumn <= rcolumn:
                middle = lcolumn + (rcolumn - lcolumn) / 2
                if target == matrix[mid][middle]:
                    return True
                if target > matrix[mid][middle]:
                    lcolumn = middle + 1
                else:
                    rcolumn = middle - 1
        return False