import heapq
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # tasks[i] = 각 작업에 필요한 힘 

        # workers[j] = 각 작업자의 힘

        # 각 작업자는 하나의 작업만 할당 받을 수 있음, 
        # 작업을 수행하려면 workers[j] >= tasks[i] 여야 한다.

        # pills = 작업자 strength만큼 증가시킬 수 있음.
        # - 각 작업자에게는 약을 최대 한 번만 줄 수 있음.

        # 완료할 수 있는 task의 최대 수 return

        low = 0
        high = min(len(tasks), len(workers)) 

        tasks.sort()
        workers.sort()

        ans = 0

        # 작업 k개를 작업자들에게 (pills개까지 써서) 배정할 수 있는지 확인
        def can_assign(k):
            selected_tasks = tasks[:k][::-1]
            selected_workers = workers[-k:]
            pills_left = pills
            available = deque(selected_workers)
            min_diff = 0

            for task in selected_tasks:
                # 가장 강한 worker가 할 수있는지
                if available and available[-1] >= task:
                    available.pop()
                elif available and pills_left > 0:
                    found = False 
                    for i in range(len(available)):
                        if available[i] + strength >= task:
                            available.remove(available[i])
                            pills_left -=1 
                            found = True
                            break
                    if not found:
                        return False
                else:
                    return False
            return True 



        while low <= high:
            mid = (low + high) // 2

            # mid 개의 작업을 할당 할 수 있는 경우 
                # 더 많이 할 수 있는지 오른쪽 탐색 
            if can_assign(mid):
                ans = mid
                low = mid + 1 
        
            else:
                high = mid - 1

        return ans 

