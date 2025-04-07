

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # return 가장 큰 subset answer 
        # (answer[i], answer[j])
        # 1. answer[i] % answer[j] == 0 or 
        # 2. answer[j] % answer[i] == 0
      
        nums.sort()
        cache = {}

        def dfs(index):
            if index == len(nums):
                return []
            if index in cache:
                return cache[index]
            
            res = [nums[index]]
            
            for j in range(index+1, len(nums)):
                if nums[j] % nums[index] == 0:
                    temp = [nums[index]] + dfs(j)
                    if len(res) < len(temp):
                        res = temp
            
            cache[index] = res
            return res
        

        answer = []
        for i in range(len(nums)):
            temp = dfs(i)
            if len(temp) > len(answer):
                answer = temp

        return answer