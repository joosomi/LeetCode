class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans = {}
        for idx, val in enumerate(nums):
            remain = target - val

            if remain in ans:
                return [ans[remain], idx]
            ans[val] = idx