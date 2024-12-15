class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        cnt = Counter(nums)

        for val, freq in cnt.items():
            if freq >= 2:
                return True

        return False 