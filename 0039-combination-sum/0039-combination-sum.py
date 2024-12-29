class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []
        def dfs (i, current, current_sum):
            if current_sum == target:
                ans.append(list(current))
                return 

            elif current_sum > target:
                return

            elif current_sum < target:
                for j in range(i, len(candidates)):
                    current.append(candidates[j])
                    dfs(j, current, current_sum + candidates[j])
                    current.pop()

        
        dfs(0, [], 0)
        return ans
            