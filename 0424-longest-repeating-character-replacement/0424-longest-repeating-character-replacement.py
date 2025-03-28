from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 동일한 문자로 이루어진 가장 긴 연속된 부분 문자열 
        # 어떻게 해야 k개의 문자 수정 -  가장 긴 연속된 문자를 만들 수 있는가?
        # - 연속하는 최장 부분 문자열의 길이 return 
    

        start, end = 0, 0
        maxLen = 0
        char = defaultdict(int)

        while end < len(s) :
            windowLen = end - start + 1

            for i in s[start:end+1]:
                char[i] += 1
            
            if (windowLen) - maxLen > k:
                start += 1
                char[s[start]] -=1
                
            else: 
                char[s[end]] += 1 
                end += 1
                maxLen = max(maxLen, max(char.values()))
            
        return maxLen
        


        