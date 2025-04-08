class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two subsets
        # sum is equal => True // not equal => False
        
        Sum = sum(nums)
       
    
        if Sum % 2 != 0:
            return False 

        dp = set()
        dp.add(0)
        target = Sum // 2  

        for i in range(len(nums)):
            nextDP = set()

            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)

            dp = nextDP

        if target in dp:
            return True
        else:
            return False
            
