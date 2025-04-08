class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 배열의 모든 요소가 서로 다름 
        # 연산  : 배열의 처음 3 요소 제거, 3개 보다 작으면
        #  - 남은 요소 전부 제거 

        cnt = 0

        while len(set(nums)) != len(nums):
            if len(nums) >= 3:
                nums = nums[3:]
            else: 
                nums = []
    
            cnt +=1 

        return cnt 
