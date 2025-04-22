from math import comb

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
        # ideal array
        # - 배열의 모든 요소는  1 이상 maxValue 이하 - (0<= i <n)
        # - 인덱스가 1이상일 때, arr[i] % arr[i-1] == 0

        # Return =  서로 다른 ideal arrays의 개수 % (10^9 + 7)

        # ideal array는 non-decreasing
        # arr[i] > arr[i-1]이어야 하는 경우 - DP
        # 조합을 활용

        MOD = 10**9 + 7

        ans = maxValue

        # 처음엔 [1], [2], [3] ... [maxValue] 다 한 개씩 있으니까 1
        # 수열 확장할 때 다음 숫자는 num의 배수만 올 수 있음 
        freq = {num: 1 for num in range(1, maxValue+1)}

        # 최종 목표 길이 = n 
        for length in range(1, n):
            cnt = Counter()
  
            for num in freq:
                for next_num in range(2, maxValue //num + 1): 
                    ans += comb(n-1, length) * freq[num]
                    cnt[next_num*num] += freq[num] # 새로운 수열의 개수 추가 
                    

            freq = cnt
            ans %= MOD
            
        return ans 
