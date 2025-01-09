class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, path, curSum):
            if curSum == target:
                res.append(path.copy())
                return 
            elif curSum > target:
                return 

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, curSum + candidates[i])
                path.pop()

        dfs(0, [], 0)
        
        return res