class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Palindrome -> 양끝을 하나씩 비교

        alphanumeric = "abcdefghijklmnopqrstuvxyz0123456789"
        
        filtered = [i for i in lower(s) if i in alphanumeric]

        left, right = 0, len(filtered)-1

        while left < right:
            if filtered[left] == filtered[right]:
                pass
            
            else:
                return False
            left += 1
            right -= 1

        return True