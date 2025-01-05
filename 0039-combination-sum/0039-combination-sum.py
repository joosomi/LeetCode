class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []

        def backtracking(idx, path, target):
            if target <0 or idx >= len(candidates):
                return 
                
            if target ==  0:
                ans.append(list(path))
                return

            path.append(candidates[idx])
            backtracking(idx, path, target - candidates[idx])
            path.pop()
            backtracking(idx+1, path, target)

        backtracking(0, [] ,target)
        return ans