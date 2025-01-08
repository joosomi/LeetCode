class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)

        Pre = 1
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = Pre * nums[i-1]
            Pre*= nums[i-1]
        
        print(output)

        Post = 1 
        for i in range(len(nums)-1, -1, -1):
            output[i] = Post * output[i]
            Post *= nums[i]

        
        return output