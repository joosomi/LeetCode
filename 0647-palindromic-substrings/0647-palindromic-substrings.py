class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        def countPalindrome(left, right):
            result = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                result += 1 
                left -=1
                right +=1
            return result 

        for i in range(len(s)):
            ans += countPalindrome(i, i)
            ans += countPalindrome(i, i+1)

        return ans 