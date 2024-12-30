class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(set(nums))
        print(n)

        for i in range(0, n+1) :
            if i not in nums:
                return i