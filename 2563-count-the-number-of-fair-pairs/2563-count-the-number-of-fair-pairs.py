class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # return the number of fair pairs
        # (i, j) : 0 <= i < j < n
        # lower <= nums[i] + nums[j] <= upper

        
        nums.sort() 

        n = len(nums)

        def helper(up):
            cnt = 0
            right = n - 1

            for left in range(n):
                while left < right and nums[left] + nums[right] > up:
                    right -=1
                cnt += max(0, right - left)
            return cnt

        return helper(upper) - helper(lower-1)

            