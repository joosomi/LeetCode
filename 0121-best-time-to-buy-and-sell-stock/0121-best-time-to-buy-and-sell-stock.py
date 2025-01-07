class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minimum = float('inf')
        profit = 0
        for i in range(len(prices)):
            minimum = min(prices[i], minimum)
            profit = max(prices[i] - minimum, profit)

            
 
        
        
        return profit

            
