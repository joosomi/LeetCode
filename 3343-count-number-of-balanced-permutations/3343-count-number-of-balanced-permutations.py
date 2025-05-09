import math 

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # 짝수 번째 자리 숫자의 합 == 홀수 번째 자리 숫자의 합 ( 균형 문자열 )

        # dp - (짝수 index의 개수, 문자,  짝수 인덱스의 합)

        MOD = 10**9 + 7
        
        total_sum = sum(map(int, num))

        # 전체 합이 홀수면 절대 balanced 문자열이 될 수 없다. 
        if total_sum % 2 != 0:
            return 0

        target_sum = total_sum // 2 # 목표 짝수 인덱스의 합 
        half_len = len(num) % 2 + len(num) // 2 # 짝수 index의 개수 
        
        cnt = Counter(num)

        dp = [[0]*(half_len+1) for _ in range(target_sum+1)]
        dp[0][0] = 1 
        
 

        for digit in list(num):
            d = int(digit)
            for s in range(target_sum, d -1 , -1):
                for k in range(half_len, 0, -1):
                    dp[s][k] += dp[s-d][k-1]

        ans = dp[target_sum][half_len] # 짝수 인덱스 조합의 수 

        ans *= math.factorial(half_len) * math.factorial(len(num) - half_len)  

        for v in cnt.values():
            ans //= math.factorial(v)

        return ans % MOD 


       