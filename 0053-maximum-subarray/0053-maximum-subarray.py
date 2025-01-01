class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0] * (len(nums))


        for i in range(len(nums)):  
                current = nums[i]
                dp[i] = max(current, dp[i-1] + current)
                
        return max(dp)