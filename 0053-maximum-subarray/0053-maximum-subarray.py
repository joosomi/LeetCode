class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane’s Algorithm
        # 현재 부분 배열의 합(cur_sum)이 음수가 되면 새로운 부분 배열을 시작한다. 
        # 추가 배열 없이 현재 상태(cur_sum)만으로 최적 해를 유지

        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
