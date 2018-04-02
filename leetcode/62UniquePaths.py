'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path=[[1]for x in range(m)]
        for i in range(1,n):
            path[0].append(1)
        for i in range(1,m):
            for j in range(1,n):
                path[i].append(path[i-1][j]+path[i][j-1])
        return path[m-1][n-1]