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

        max_value = 0
        max_i_value = nums[0]
        for j in range(1, len(nums)):
            max_i_value = max(max_i_value, nums[j-1])
            i =  nums.index(max_i_value)
            for k in range(j+1, len(nums)):
                max_value = max(max_value, (nums[i]- nums[j])*nums[k])

        return max_value
            
                    