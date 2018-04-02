class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        length = len(word)
        if length == 0:
            return True
        self.row = len(board)
        self.column = len(board[0])
        visited = [[0 for i in range(self.column)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                if board[i][j] == word[0]:
                    a = visited
                    if self.dfs(i, j, word[1:], board, a):
                        return True
        return False

    def dfs(self, x, y, word, board, visited):
        if len(word) == 0:
            return True
        if x > 0 and board[x - 1][y] == word[0] and visited[x - 1][y] != 1:
            visited[x][y] = 1
            if self.dfs(x - 1, y, word[1:], board, visited):
                return True
        if x < (self.row - 1) and board[x + 1][y] == word[0] and visited[x + 1][y] != 1:
            visited[x][y] = []
            if self.dfs(x + 1, y, word[1:], board, visited):
                return True
        if y > 0 and board[x][y - 1] == word[0] and visited[x][y - 1] != 1:
            visited[x][y] == 1
            if self.dfs(x, y - 1, word[1:], board, visited):
                return True
        if y < (self.column - 1) and board[x][y + 1] == word[0] and visited[x][y + 1] != 1:
            visited[x][y] = 1
            if self.dfs(x, y + 1, word[1:], board, visited):
                return True
        return False


