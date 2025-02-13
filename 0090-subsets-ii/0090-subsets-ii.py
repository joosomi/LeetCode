class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        def backtrack(idx, current):
            if current.copy() not in ans:
                ans.append(current.copy())
            for i in range(idx, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()

        backtrack(0, [])
        return ans
