class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        #rotate the array to the right by k steps
        
        ans = nums[:] # 복사해서 새로운 배열 생성 
        k = k % len(nums)

        for i, v in enumerate(nums):
            nums[(i + k) % len(nums)] = ans[i]

        return nums