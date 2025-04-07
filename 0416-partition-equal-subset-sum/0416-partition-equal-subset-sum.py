class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two subsets
        # sum is equal => True // not equal => False
        
        Sum = sum(nums)
        
        visited = set()

        if Sum % 2 != 0:
            return False 

        def dfs(index, current_sum):
            if current_sum == Sum//2:
                return True

            if index == len(nums) -1:
                return False

            if (index, current_sum) in visited:
                return False

            visited.add((index, current_sum))
        
            return dfs(index+1, current_sum + nums[index]) or dfs(index+1, current_sum)

        return dfs(0, 0)