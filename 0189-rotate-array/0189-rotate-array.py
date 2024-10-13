class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        #rotate the array to the right by k steps
        #return 값은 상관이 없는 문제

        ### solution 1. 
        # ans = nums[:] # 복사해서 새로운 배열 생성 
        # k = k % len(nums)

        # for i, v in enumerate(nums):
        #     nums[(i + k) % len(nums)] = ans[i]

        ### solution 2. 
        #  nums[-k:]는 배열의 마지막 k개의 요소
        #  nums[:-k]는 배열의 처음부터 끝에서 k번째 앞까지의 요소
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

        
         