class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Palindrome -> 양끝을 하나씩 비교

        alphanumeric = "abcdefghijklmnopqrstuvxyz0123456789"
        
        fil = [i for i in lower(s) if i in alphanumeric]
        print(fil)
        
        for i in range(len(fil)):
            if fil[i] != fil[len(fil)-i-1]:
                return False

        return True