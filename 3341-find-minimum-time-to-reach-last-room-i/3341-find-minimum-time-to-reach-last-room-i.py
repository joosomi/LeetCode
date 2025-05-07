import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # 방 (n-1, m-1)까지 가는 데 필요한 최소 시간 Return 

        # moveTime[i][j]는 해당 방으로 이동을 시작할 수 있는 최소 시간
        # 인접한 방 이동 -  1초

        n = len(moveTime)
        m = len(moveTime[0])
        
        visited = [[float("inf")]* m for _ in range(n)]
        visited[0][0] = 0

        heap = [(0, 0, 0)]

        while heap:
            # 현재까지 이동 시간, 위치 
            curr_time, x, y = heapq.heappop(heap)

        

            # 이미 방문했다면 스킵 
            if curr_time > visited[x][y]:
                continue 

            if x == n-1 and y == m-1:
                return curr_time
            
          

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    next_time = max(curr_time, moveTime[nx][ny]) + 1

                    if next_time < visited[nx][ny]:
                        heapq.heappush(heap, (next_time, nx, ny))
                        visited[nx][ny] = next_time

        
        return 0