class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
       # 조건을 만족하는 인덱스 (i,j,k) i< j< k
       # (nums[i] - nums[j]) * nums[k]
       # 이 값을 최대로 만드는 경우를 찾아서 최대값 리턴 
       # 모든 (i,j,k) 조합의 값이 음수라면 0을 리턴
        ans = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    ans.append((nums[i] - nums[j])*nums[k])

        print(ans)

        for i in ans:
            if i > 0:
                return max(ans)
        return 0
        
        

                    