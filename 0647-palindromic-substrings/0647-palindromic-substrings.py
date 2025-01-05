class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0
        n = len(s)

        def countFromCenter(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count +=1
                left -=1 
                right +=1 
            return count
        
        for i in range(n):
            ans += countFromCenter(i, i)
            ans += countFromCenter(i, i+1)
        return ans