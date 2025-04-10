from functools import lru_cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    # powerful integer x
    # - s를 suffix(접미사)로 가진다. 끝 부분이 s
    # - x의 모든 자리 숫자는 limit 이하의 숫자
    # Return [start ~ finish] 범위 안에 있는 정수들 중 powerful 숫자 개수 
    
    # digit DP - count powerful integers in range [1, x]
    # DP[i][j]
    # - i : 지금까지 만든 숫자의 자릿수 
    # - j : 지금만든 숫자와 x를 비교한 결과
    #   j == 0 : 지금까지 만든 숫자가 x i자리까지 일치
    #   j == 1 : 지금까지 만든 숫자가 작음, 이후 자리는 자유롭게 선택 가능
    # =>  각 자리수마다 지금까지 만든 숫자가 x와 같은지 여부를 저장
    # - answer : count[finish] - count[start-1]

        def count(x):
            x_str = str(x)

            @lru_cache(None)
            def dfs(pos, tight, suffix):
                length = len(x_str)
                
                if length == pos:
                    if  ''.join(map(str, suffix)) == s:
                        return 1
                    return 0

                cnt  = 0
                max_digit = min(int(x_str[pos]), limit) if tight else limit
                
                for d in range(max_digit + 1):

                    if tight and d == int(x_str[pos]):
                        new_tight = True
                    else:
                        new_tight = False

                    new_suffix = (suffix + (d, ))

                    if len(new_suffix) > len(s):
                        new_suffix = new_suffix[1:]
                    
                    cnt += dfs(pos + 1, new_tight, new_suffix)

                return cnt 
            
            return dfs(0, True, ())


        return count(finish) - count(start-1)