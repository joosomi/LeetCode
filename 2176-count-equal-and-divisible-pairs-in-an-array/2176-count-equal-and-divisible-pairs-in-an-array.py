class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # (i, j) 0<=i<j<n, nums[i] == nums[j] and (i * j) is divisible by k

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    ans+=1
        return ans