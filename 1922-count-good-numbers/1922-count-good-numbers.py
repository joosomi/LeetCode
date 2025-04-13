class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # good number : 짝수 - 짝수 / 홀수 인덱스 - 2, 3, 5, 7 (소수)
        # return 길이가 n인 좋은 숫자 문자열의 개수  % (10^8 + 7)
        
        
        # 지수를 2진수로 쪼개면 곱셈 횟수를 줄일 수 있다.

        MOD = 10**9 + 7 

        half = ((n+1) // 2)
        odd_half = (n // 2) 

        ans = (pow(5, half,  MOD) * pow(4, odd_half,  MOD)) % MOD
        # ans = ((5**(half))*(4**(odd_half))) % (MOD)

        return ans
