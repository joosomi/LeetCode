import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        

        n = len(moveTime)
        m = len(moveTime[0])

        visited = [[[float("inf")] * 2 for _ in range(m)] for _ in range(n)]
        print(visited) 
        visited[0][0][0] = 0
        
        heap = []
        heapq.heappush(heap, (0, 0, 0, 0))

        while heap:
            moves, x, y, next_one = heapq.heappop(heap)

            if x == n -1 and y == m-1:
                return moves
            
            
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and moveTime[nx][ny] != float("inf"):     
                          
                    cost = 1 if next_one == 0 else 2 
                    new_next=  1- next_one
                    newTime = max(moves, moveTime[nx][ny]) + cost
                    
                    if visited[nx][ny][newTime % 2] > newTime:
                        visited[nx][ny][newTime % 2] = newTime
                        heapq.heappush(heap, (newTime, nx, ny, new_next))

        

