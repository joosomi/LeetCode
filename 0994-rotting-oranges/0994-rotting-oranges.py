from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 모든 오렌지가 썩는 최소 시간? - BFS

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

     
        cntz = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: #썩은 오렌지 
                    queue.append((i, j))
                    cntz +=1
                elif grid[i][j] ==1:
                    cntz+=1

        if cntz == 0:
            return 0

        direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        count = 0

        while queue:
            level_size = len(queue) 

            for _ in range(level_size):
                r, c = queue.popleft()
      
                
                for i in range(4):
                    new_r, new_c = r + direct[i][0], c + direct[i][1]
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))
            
            count += 1 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return count -1 
        