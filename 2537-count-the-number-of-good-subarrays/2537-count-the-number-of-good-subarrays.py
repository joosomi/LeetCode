from collections import defaultdict 

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Return the number of good subarrays of nums
        # 최소 K개의 쌍, (i, j) i < j and arr[i] == arr[j]

        # [l, r] - 같은 숫자 쌍이 k개 이상인지 확인
        
        n= len(nums)
        
        left, pair_cnt = 0, 0
        ans = 0
        count = defaultdict(int)

        for right, value in enumerate(nums):
            pair_cnt += count[value]
            count[value] += 1

            while pair_cnt >= k:
                ans += n - right # 왜냐하면 한번 good이면 뒤에도 다 good subarray가 된다. 
                
                count[nums[left]] -=1
                pair_cnt -= count[nums[left]]
                left +=1

        return ans