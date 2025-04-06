class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # return 가장 큰 subset answer 
        # (answer[i], answer[j])
        # 1. answer[i] % answer[j] == 0 or 
        # 2. answer[j] % answer[i] == 0
        
    
        nums.sort()

        dp = [1]*len(nums)
        prev = [-1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    
        
        max_dp = max(dp)
        print(max_dp)
        print(prev)  
        answer = []

        index = dp.index(max_dp)
        while index != -1:
            answer.append(nums[index])
            index = prev[index]

        return answer