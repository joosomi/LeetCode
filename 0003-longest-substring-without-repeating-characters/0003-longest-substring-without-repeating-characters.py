class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        start = 0
        cnt = defaultdict(int)

        for end in range(len(s)):
            cnt[s[end]] += 1
       
            while cnt[s[end]] > 1:
                cnt[s[start]] -= 1
                start += 1
            
            ans = max(ans, end-start+1)
            

        return ans
