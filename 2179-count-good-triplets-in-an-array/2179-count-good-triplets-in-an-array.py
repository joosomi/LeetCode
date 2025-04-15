# from itertools import combinations
from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # good triplets: x, y, z 
        # - nums1 : pos1[x] < pos1[y] < pos1[z]
        # - nums2: pos2[x] < pos2[y] <pos2[z]
        

        # 두 배열에서 모두 오름차순인 (x, y, z) 조합의 개수
        # - y가 중간값일 때 
        # - 그 앞에 올 수 있는 x의 개수 * 그 뒤에 올 수 있는 z의 개수를 구해야 한다. 
        
        ans = 0
        n = len(nums1)

        pos2 = {val: idx for idx, val in enumerate(nums2)}
        mapped = [pos2[val] for val in nums1]

        left = SortedList()
        right = [0]*n

        seen = SortedList()

        for i in range(n-1, -1, -1):
            y = mapped[i]
            right[i] = len(seen) - seen.bisect_right(y)
            seen.add(y)

        for i in range(n):
            y = mapped[i]
            x_count = left.bisect_left(y)
            z_count = right[i]
            ans += x_count * z_count
            left.add(y)
        
        return ans 