class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 1-1. Sliding Window -> O(N)
        # 
        # current_sum = sum(nums[0:k])
        # max_sum = current_sum

        # for i in range(k, len(nums)):
        #     current_sum += nums[i] - nums[i-k]

        #     max_sum = max(max_sum, current_sum)
        
        # return float(max_sum) / k

        # 1-2.
        # if len(nums) ==1 :
        #     return float(nums[0])

        # start, end = 0, k
        # average = 0.0

        # for i in range(k):
        #     average += float(nums[i]) / k
        
        # max_average = average 

        # while end < len(nums):
        #     average = average - float(nums[start]) / k
        #     average = average + float(nums[end]) / k
        #     max_average = max(max_average, average)

        #     start += 1
        #     end +=1 

        # return max_average 

        # 2. 
        cur = 0
        for i in range(k):
            cur += nums[i]
        
        max_sum = cur
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            if cur > max_sum:
                max_sum = cur
        
        return float(max_sum) / k