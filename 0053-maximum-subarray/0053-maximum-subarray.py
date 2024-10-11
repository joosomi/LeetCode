class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #가장 합이 큰 subarray를 찾고 return sum
        #subarray: 그냥 부분 배열이 아닌 연속된 부분배열!!!! 
        
        # O(n)의 solution을 찾았다면,
        # divide and conquer approach solution 구현해보기
    
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            
            max_sum = max(max_sum, current_sum)
            
        return max_sum
            
            