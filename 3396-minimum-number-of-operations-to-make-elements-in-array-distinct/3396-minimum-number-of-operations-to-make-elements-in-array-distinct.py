class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 배열의 모든 요소가 서로 다름 
        # 연산  : 배열의 처음 3 요소 제거, 3개 보다 작으면
        #  - 남은 요소 전부 제거 

        ans = 0
        count = set()

        for idx, val in enumerate(reversed(nums)):
            if val in count:
                ans = ((len(nums) - idx - 1) // 3) + 1 
                return ans
            else:
                count.add(val)       

        return ans
