class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        current = []
        result = []

        def dfs(i, candidates_sum):

            if candidates_sum == target :
                result.append(list(current))
            
            elif candidates_sum < target :
                for j in range(i, len(candidates)):
                    current.append(candidates[j])
                    dfs(j, candidates_sum + candidates[j])
                    current.pop()
        

        dfs(0,0)
        return result



 