class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 조건을 만족하는 인덱스 (i,j,k) i< j< k
        # (nums[i] - nums[j]) * nums[k]
        # 이 값을 최대로 만드는 경우를 찾아서 최대값 리턴 
        # 모든 (i,j,k) 조합의 값이 음수라면 0을 리턴

        # max_value 값이 음수라면, 결국에는 모든 조합의 값이 음수라는 의미! 

        # max_value = 0 

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             max_value = max(max_value, (nums[i] - nums[j])*nums[k])

        # return max_value


        max_value, max_i_val, max_sub = 0, 0, 0

        for i in nums:           
            max_value = max(max_sub * i, max_value)
            max_i_val = max(i, max_i_val)
            max_sub = max(max_i_val - i, max_sub)
            

        return max_value