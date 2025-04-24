class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # complete arrays의 수 
        # - 서로 다른 숫자의 개수가 원래 배열 전체에 있는 서로 다른 숫자의 개수와 같아야 함 

        # k = 서로 다른 원소의 개수
        # 구해야 하는 것: k개의 서로 다른 원소를 포함한 subarray의 개수
        # 입력값이 찾아서 브루트포스도 가능
        
        n = len(nums)
        ans = 0
        total_distinct = len(set(nums))
        
        
        for left in range(n):
            cnt = defaultdict(int)
            distinct = 0
            
            for right in range(left, n):
                if cnt[nums[right]] == 0:
                    distinct +=1
                cnt[nums[right]] += 1

                if distinct == total_distinct:
                    ans +=1 
                elif distinct > total_distinct:
                    break

        return ans 