class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx, current):
            ans.append(current.copy())
            for i in range(idx, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()

        backtrack(0, [])
        return ans   
