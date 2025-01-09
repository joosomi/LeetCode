class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(i, current, total):
            if total == target:
                ans.append(current[:]) #복사본 저장 
                return 
            
            if total > target or i >= len(candidates):
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return ans