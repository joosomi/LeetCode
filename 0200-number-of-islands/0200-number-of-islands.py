class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        ans = 0
        visited = [[False for _ in range(rows)] for _ in range(cols)]

        def dfs(c, r):
            
            if c < 0 or r<0 or c>= cols or r>= rows or visited[c][r] or grid[c][r] != "1":
                return False
    
            visited[c][r] = True

            dfs(c-1, r)
            dfs(c+1, r)
            dfs(c, r-1)
            dfs(c, r+1)
            
            return True

        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    ans +=1 
            
        return ans