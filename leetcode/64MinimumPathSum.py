#encoding:utf-8
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        path = [[0 for i in range(column)] for i in range(row)]
        path[0][0] = grid[0][0]
        for i in range(1, column):
            path[0][i] = path[0][i - 1] + grid[0][i]
        for i in range(1, row):
            path[i][0] = path[i - 1][0] + grid[i][0]
        for i in range(1, column):
            for j in range(1, row):
                path[j][i] = grid[j][i] + min(path[j - 1][i], path[j][i - 1])
        return path[row - 1][column - 1]
