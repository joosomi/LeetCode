class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index, value):
            if index == len(nums):
                return value

            value ^= nums[index]
        
            return  dfs(index+1, value^nums[index]) + dfs(index+1, value)


        return dfs(0, 0)