class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
      
        visited = [[0 for _ in range(m)] for _ in range(n)]
        print(visited)
        print(m)
        print(n)

        def dfs(x, y, idx):
            if idx == len(word):
                return True
            elif x <0 or x>= n or y <0 or y >=m:
                return False
            elif visited[x][y]:
                return False
            elif  board[x][y] != word[idx]:
                return False

            visited[x][y] = True

            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if dfs(nx, ny, idx+1):
                    return True

            visited[x][y] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False

        