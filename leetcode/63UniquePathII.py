#including:utf-8
def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    row = len(obstacleGrid)
    column = len((obstacleGrid[0]))
    path = [[0 for i in range(column)] for j in range(row)]
    for i in range(column):
        if obstacleGrid[0][i] != 1:
            path[0][i] = 1
        else:
            break
    print(path)
    for i in range(1, row):
        if obstacleGrid[i][0] != 1:
            path[i][0] = 1
        else:
            break
    print(path)
    for i in range(1, column):
        for j in range(1, row):
            if obstacleGrid[j][i] == 1:
                path[j][i] = 0
            else:
                path[j][i] = path[j - 1][i] + path[j][i - 1]
    print( path[row - 1][column - 1])
obstacleGrid=[[1,0][0,0]]
uniquePathsWithObstacles(obstacleGrid)
