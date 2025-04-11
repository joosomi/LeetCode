class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Return [low, high] 안에 있는 대칭적인 정수의 개수
        cnt = 0

        for num in range(low, high + 1):
            str_num = str(num)

            if len(str_num) % 2 != 0:
                continue
            
            pos = len(str_num)
            half_pos = len(str_num) // 2 

            half = sum(map(int, str_num[:half_pos]))
            other_half = sum(map(int, str_num[half_pos: ]))

            if half == other_half:
                cnt+=1
            

        
        return cnt

            