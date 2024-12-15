class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Palindrome -> 양끝을 하나씩 비교

        filtered = [i for i in lower(s) if i.isalnum()]

        return filtered == filtered[::-1]