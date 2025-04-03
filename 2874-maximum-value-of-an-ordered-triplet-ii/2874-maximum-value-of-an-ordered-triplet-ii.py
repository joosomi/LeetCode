class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 최대값 (nums[i] - nums[j] * nums[k]) : (i < j < k)
        
        max_value = 0
        i_val = 0
        diff_val = 0 
        for n in nums:
            max_value = max(max_value, diff_val * n )
            i_val = max(i_val, n)
            diff_val = max(diff_val, i_val - n)

        return max_value