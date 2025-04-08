class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two subsets
        # sum is equal => True // not equal => False
        
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        

        def dfs(idx, current_sum):
            if current_sum == sum(nums)//2:
                return True
            if idx == len(nums) - 1 :
                return False
            
            if (idx, current_sum) in dp:
                return False

            dp.add((idx, current_sum))
            return dfs(idx+1, current_sum) or dfs(idx+1, current_sum + nums[idx])
        
        return dfs(0, 0)

