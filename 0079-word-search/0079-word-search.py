class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        c = len(board[0])
        r = len(board)
        visited = [[False]* c for _ in range(r)]

        def dfs(idx, x, y, path):
            if  idx == len(word):
                return True
            elif x <0 or y <0 or x>= r or y>= c:
                return 
            elif visited[x][y] or board[x][y] != word[idx]:
                return 

            visited[x][y] = True
            path.append(board[x][y])
            
            if  dfs(idx+1, x+1, y, path) or \
                dfs(idx+1, x, y+1, path) or \
                dfs(idx+1, x-1, y, path) or \
                dfs(idx+1, x, y-1, path):
                    return True

            path.pop()
            visited[x][y] = False
   
        for i in range(r):
            for j in range(c):
                if dfs(0, i, j, []):
                    return True
        return False