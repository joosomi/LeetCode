class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #Sliding Window -> O(N)

        current_sum = sum(nums[0:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]

            max_sum = max(max_sum, current_sum)
        
        return float(max_sum) / k