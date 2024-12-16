class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans = []
        for idx, val in enumerate(nums):
            remain = target - val

            if remain in nums and nums.index(remain) != idx:
                ans.append(nums.index(remain))
                ans.append(idx)
                return ans