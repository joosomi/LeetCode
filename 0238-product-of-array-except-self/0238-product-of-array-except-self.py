class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)

        Pre = 1
        for i in range(len(nums)):
            output[i] = Pre 
            Pre *= nums[i]
        
        print(output)

        Post = 1 
        for i in range(len(nums)-1, -1, -1):
            output[i] *= Post
            Post *= nums[i]

        
        return output