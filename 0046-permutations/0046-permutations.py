class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False]* len(nums)
        def backtrack(idx, path):
            cur = path.copy()
            if len(cur) == len(nums):
                ans.append(cur)

            for i in range(len(nums)):
                if used[i] == False:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(idx+1, path)

                    path.pop()
                    used[i] = False

        backtrack(0, [])
        return ans


            
