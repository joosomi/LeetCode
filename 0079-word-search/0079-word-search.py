class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        cols = len(board)
        rows = len(board[0])
        visited = [[False for _ in range(rows)] for _ in range(cols)]
 
        def dfs(c, r, length):
            if c >= cols or r >= rows or c<0 or r<0:
                return False
            if board[c][r] != word[length] or visited[c][r]:
                return False
            if length == len(word)-1:
                return True

            visited[c][r]=True
            
            if dfs(c+1, r, length+1):
                return True
            elif dfs(c, r+1, length+1):
                return True
            elif dfs(c-1, r, length+1):
                return True
            elif dfs(c, r-1, length+1):
                return True

            visited[c][r] = False 
            return False

        for co in range(cols):
            for ro in range(rows):
                if dfs(co, ro, 0):
                    return True
        return False
        
