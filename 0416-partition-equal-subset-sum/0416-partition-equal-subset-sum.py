class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two subsets
        # sum is equal => True // not equal => False
        
        Sum = sum(nums)
        n = len(nums)

        if Sum % 2 != 0:
            return False
        
        target = Sum // 2 
        dp = [False]*(target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i- num]

        return dp[target]