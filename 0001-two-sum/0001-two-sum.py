class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for idx, val in enumerate(nums):
            if target - val in nums[idx+1:]:
                ans.append(idx)
                ans.append(nums[idx+1:].index(target-val)+idx + 1 )
                return ans

            else:
                pass

        