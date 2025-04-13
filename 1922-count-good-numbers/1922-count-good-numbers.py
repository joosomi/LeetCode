class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # good number : 짝수 - 짝수 / 홀수 인덱스 - 2, 3, 5, 7 (소수)
        # return 길이가 n인 좋은 숫자 문자열의 개수  % (10^8 + 7)
        
        
        # 지수를 2진수로 쪼개면 곱셈 횟수를 줄일 수 있다.

        MOD = 10**9 + 7 

        half = bin((n+1) // 2)
        odd_half = bin(n // 2) 

        bin_half, bin_odd_half = half[1:], odd_half[1:]
        half_len, odd_half_len = len(bin_half), len(bin_odd_half)

        even_pow, odd_pow = 0, 0

        for i in range(half_len):
            power = half_len - 1 - i 
            if bin_half[i] == '1':
                even_pow += ( 2**power )

        for i in range(odd_half_len):
            power = odd_half_len - 1 - i 
            if bin_odd_half[i] == '1':
                odd_pow += ( 2**power )

        ans = (pow(5, even_pow,  MOD) * pow(4, odd_pow,  MOD)) % MOD
        # ans = ((5**(half))*(4**(odd_half))) % (MOD)

        return ans
