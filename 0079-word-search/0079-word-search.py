class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, idx):
            if len(path) == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            if (r, c) in path:
                return False
            if word[idx] != board[r][c]:
                return False

            path.add((r,c))
            
            if dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or  dfs(r, c-1, idx+1):
                return True
            
            path.remove((r,c))
            return False
            
     
            

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
            
        return False