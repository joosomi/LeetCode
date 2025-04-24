class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # complete arrays의 수 
        # - 서로 다른 숫자의 개수가 원래 배열 전체에 있는 서로 다른 숫자의 개수와 같아야 함 

        # k = 서로 다른 원소의 개수
        # 구해야 하는 것: k개의 서로 다른 원소를 포함한 subarray의 개수
        # 입력값이 찾아서 브루트포스도 가능
        
        ans = 0
        k = len(set(nums))


        for i in range(len(nums)):
            counter = defaultdict(int)
            for j in range(i, len(nums)):
                counter[nums[j]] += 1
                if len(counter) == k:
                    ans +=1

        return ans 