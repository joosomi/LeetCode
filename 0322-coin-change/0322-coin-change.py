class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        
        dp =[float('inf')] * (amount + 1)
        dp[0] = 0


        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i-c]+1, dp[i])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
