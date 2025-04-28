class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #배열의 점수는 배열의 합과 길이의 곱 
        # Return - 비어있지 않은 subarray의 개수 (score가 k보다 작은)


        left = 0
        ans = 0
        total = 0

        for right in range(len(nums)):
            total += nums[right]
           
           
            while left<= right and (total * (right - left + 1)) >= k:
                total -= nums[left]
                
                left +=1 
            
            ans += right - left + 1 
        
        return ans 