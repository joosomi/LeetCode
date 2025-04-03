class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 최대값 (nums[i] - nums[j] * nums[k]) : (i < j < k)
        
        # prefix 최대 배열, suffix 최대 배열을 미리 계산
        # - prefix_max[i] : max(nums[0] ~ nums[i])
        # - suffix_max[i] : max(nums[i] ~ nums[n-1])
        # Return (prefix_max[j-1] - nums[j]) * suffix_max[j+1]

        prefix_max = [0] * len(nums)
        prefix_max[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_max=  [0] * len(nums)
        suffix_max[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])

        answer = 0
        
        for j in range(1, len(nums)-1):
            prefix = prefix_max[j-1]
            suffix = suffix_max[j+1]

            answer = max(answer, (prefix - nums[j]) * suffix)
        return answer