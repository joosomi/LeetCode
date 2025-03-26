class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 모든 가능한 substrings 체크 
        # -> valid 인 경우, maxLen 계속 업데이트

        chars = dict()

        for i in range(len(s)):
            chars[s[i]] = i # 마지막 위치 인덱스를 저장

        maxLen = 0

        left, right = 0, 0
        
        check_duplicate = set()

        while right < len(s):
            # 중복되는 경우
            if s[right] in check_duplicate:
                check_duplicate.remove(s[left])
                left += 1

            else:      
                check_duplicate.add(s[right])
                right += 1
                Len = right - left 
                maxLen = max(maxLen, Len)


        return maxLen