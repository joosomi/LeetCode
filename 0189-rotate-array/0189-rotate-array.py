class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        #rotate the array to the right by k steps
        
        ans = nums[:]
        k = k % len(nums)

        for i, v in enumerate(nums):
            nums[(i + k) % len(nums)] = ans[i]

        return ans