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
    
#         max_sum = nums[0]
#         current_sum = nums[0]
        
#         for i in range(1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])
            
#             max_sum = max(max_sum, current_sum)
            
#         return max_sum
        
      
        def maxSub(A, L, R):
            if L == R:
                return A[L]
            if L > R:
                return  -10**9
            
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            
            #왼쪽에서 중간으로
            for i in range(mid-1, L-1, -1):
                cur_sum = cur_sum + A[i]
                left_sum = max(left_sum, cur_sum)
            
            cur_sum =0
            
            #오른쪽에서 중간으로
            for i in range(mid+1, R+1):
                cur_sum = cur_sum + A[i]
                right_sum = max(right_sum, cur_sum)
                
            cross_sum =  left_sum + A[mid] + right_sum
            
            return max(maxSub(A, L, mid-1), maxSub(A, mid+1, R), cross_sum)
        
        return maxSub(nums, 0, len(nums)-1)
            
            
            
            