class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        hset = set()

        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            else:
                hset.add(nums[i])
        return False