
from collections import Counter
from math import factorial 

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Return n자리 숫자 중에서 good integers의 개수 
        # - 앞자리 0이 오는 숫자는 X 

        # 순열 - 재배열을 하면 K 팰린드롬이 될 수 있는 
        # 팰린드롬 - 좌/우 대칭
        # 홀수 - 중앙에 1개, 나머지는 짝수 개수로 존재

        # - 1. 팰린드롬이 되어야 한다.
        # - 짝수 길이 : 모든 숫자 등장 짝수
        # - 홀수 길이 : 홀수 개로 등장하는 숫자가 딱 1개

        # 2. 실제 팰린드롬을 만들고 if % k == 0이면 cnt +=1 
        # 3. set을 사용하여 중복 제거하여 계산
        ans = set()
        half_len = (n+1) // 2 
        cnt = 0
        visited = set()


        start = 10**(half_len - 1)
        end = 10**(half_len)

        for num in range(start,end):
            s = str(num)
            if n % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[:-1][::-1]
            
            if int(pal) % k != 0:
                continue
            
            digits=  tuple(sorted(pal))
            if digits in visited:
                continue
            visited.add(digits)

            freq = Counter(digits)

            total = factorial(n) 

            for v in freq.values():
                total //= factorial(v)

            if freq['0'] > 0:
                freq['0'] -=1
                invalid = factorial(n-1) # 앞자리에 0이 오는 숫자의 개수
                for v in freq.values():
                    invalid //= factorial(v)
                freq['0'] += 1
                total -= invalid # 유효하지 않은 수 제외
            
            cnt += total
                
        return cnt
