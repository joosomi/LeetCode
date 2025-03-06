class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1

        while left < right and right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0

            left +=1
            right+=1
            
        nums.sort(key=lambda x: (x == 0))
        return nums