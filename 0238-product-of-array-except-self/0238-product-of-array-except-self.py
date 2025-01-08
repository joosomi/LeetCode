class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]*len(nums)
        postfix = [nums[-1]]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
        
        for j in range(len(nums)-2, -1, -1):
            print(j)
            postfix[j] = postfix[j+1] * nums[j]

        print(postfix)
        ans = [1]*len(nums)
        for k in range(len(nums)):
            if k == 0:
                ans[k] = postfix[1]
            elif k == len(nums)-1:
                ans[k] = prefix[k-1]
            else:
                ans[k] = prefix[k-1] * postfix[k+1]
        
        return ans
        