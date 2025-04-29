class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 최대 원소 크기가 subarray 안에 적어도 K번 나오는 subarray의 개수 

        MAX = max(nums)

        left = 0
        ans = 0
        max_count = 0  

        for right in range(len(nums)):
           
            if nums[right] == MAX:
                max_count += 1 
                
            while max_count >= k:
                ans += len(nums) - right 
                
                if nums[left] == MAX:
                    max_count -=1

                left += 1 

        return ans 
