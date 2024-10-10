class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}

        for i, v in enumerate(nums):
            ans = target - v 

            if ans in dict:
                return [dict[ans], i]
            dict[v] = i

        return []