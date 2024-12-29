class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # prefix, suffix 곱을 미리 계산하기 
        ans = [1]*len(nums)
        suffix = []

        for i in range(1, len(nums)):
            if len(ans) == 0:
                ans[0] = nums[0]
            else:
                ans[i] = nums[i-1]*ans[i-1]

        for i in range(len(nums)-1, -1, -1):
            if len(suffix) == 0:
                suffix.append(nums[i])
            else:
                suffix.append(nums[i]*suffix[-1])

        suffix.reverse()

        print(ans, suffix)

        for i in range(len(nums)):
            if i == 0 :
                ans[i] = suffix[i+1]
            elif i == len(nums)-1:
                ans[i] = ans[-1]
            else:
                ans[i] = ans[i]*suffix[i+1]


        return ans