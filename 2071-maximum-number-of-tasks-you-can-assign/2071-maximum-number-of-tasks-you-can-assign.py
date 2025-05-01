from bisect import bisect_left
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
        workers.sort(reverse = True)
        n = len(tasks)
        ans = 0

        # 작업 k개를 작업자들에게 (pills개까지 써서) 배정할 수 있는지 확인
        def can_assign(k, pills_left):
            task_idx = 0
            task_temp = deque()

            # 가장 강한 k명의 작업자들을 순회 
            for i in range(k-1, -1, -1):
                while task_idx < k and tasks[task_idx] <= workers[i] + strength:
                    task_temp.append(tasks[task_idx])
                    task_idx +=1 

                if len(task_temp) == 0:
                    return False

                if workers[i] >= task_temp[0]: # 약 안써도 가능한 작업인 경우 
                    task_temp.popleft()

                elif pills_left > 0:
                    task_temp.pop() # 가장 어려운 작업을 약 먹고 수행 
                    pills_left -=1
                else:
                    return False
            return True



        while low <= high:
            mid = (low + high) // 2

            # mid 개의 작업을 할당 할 수 있는 경우 
                # 더 많이 할 수 있는지 오른쪽 탐색 
            if can_assign(mid, pills):
                ans = mid
                low = mid + 1 
        
            else:
                high = mid - 1

        return ans 

