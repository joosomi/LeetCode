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
        # k = k % len(nums)
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]

        ### solution 3. 
        # ex. [ 1, 2, 3, 4, 5, 6, 7], k = 3 
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1 , end - 1 

        n = len(nums)
        k %= n          
        reverse(0, n-1) # [7, 6, 5, 4, 3, 2, 1]
        reverse(0, k-1) # [5, 6, 7, 4, 3, 2 , 1]
        reverse(k, n-1) # [5, 6, 7, 1, 2, 3, 4]