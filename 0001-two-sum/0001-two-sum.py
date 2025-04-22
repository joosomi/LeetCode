class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            num = target - nums[i]

            if num in h:
                return [i, h[num]]
            
            h[nums[i]] = i
        
