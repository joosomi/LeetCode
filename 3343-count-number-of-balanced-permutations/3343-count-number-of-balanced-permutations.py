import math 

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # 짝수 번째 자리 숫자의 합 == 홀수 번째 자리 숫자의 합 ( 균형 문자열 )

        # dp - (짝수 index의 개수, 문자,  짝수 인덱스의 합)

        MOD = 10**9 + 7
        
        n = len(num)
        cnt = Counter(int(ch) for ch in num)
        total_sum = sum(int(ch) for ch in num)

        if total_sum % 2 != 0:
            return 0

        half_sum = total_sum // 2
        odd = n // 2 
        even = n - odd

        # balance = 짝수 인덱스 합 - 홀수 인덱스 합  => target = 0

        @cache
        def dfs(digit, odd_left, even_left, balance):
            # 종료 조건
            if digit < 0:
                return int(odd_left == 0 and even_left == 0 and balance == 0)

            ans = 0

            # 해당 digit이 나온 횟수 -> 홀수/짝수 index에 몇개를 넣을 것인지 
            for take_from_odd in range(cnt[digit] + 1):
                take_from_even = cnt[digit] - take_from_odd 

                if take_from_odd > odd_left or take_from_even > even_left:
                    continue

                # 조합할 수 있는 경우의 수 
                ways = comb(odd_left, take_from_odd) * comb(even_left, take_from_even) 
                new_balance = balance - digit * (take_from_even - take_from_odd)

                ans += ways * dfs(digit-1, odd_left - take_from_odd, even_left - take_from_even, new_balance)
                ans %= MOD

            
            return ans 


        return dfs(9, odd, even, 0)

