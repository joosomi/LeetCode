class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # nice 한 subarray(연속 배열)?
        # - 서로 다른 두 숫자 - bit & 연산 = 0 

        left = 0
        bit_mask = 0
        ans = 0

        for right in range(len(nums)): 
            while (bit_mask & nums[right]) != 0:
                bit_mask ^= nums[left] # XOR 연산자 
                left += 1
            bit_mask |= nums[right] # OR 연산자
            ans = max(ans, right-left +1)


        return ans
                