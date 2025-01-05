class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        
        dp[0] = 0 
        print(nums[0])
        dp[1] = nums[0]
        print(dp)
        
        for i in range(2, len(nums)+1):
            # 비교하면서 최댓값을 갱신하기
            dp[i] = max(dp[i-1]+nums[i-1], nums[i-1])
        
        print(dp)
        return max(dp[1:])
