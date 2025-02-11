class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 섬의 최대 영억 크기 

        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or c < 0 or r>= rows or c >= cols:
                return False
            if grid[r][c] != 1:
                return False
            if visited[r][c]:
                return False

            visited[r][c] = True

            area = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return area
        
        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1  and not visited[i][j]:
                    max_island = max(dfs(i,j), max_island)

        
        return max_island
