class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2+ str1:
            return ""
        
        # def gcd(a, b):
        #     while b:
        #         a, b = b, a % b
        #     return a

        # gcd_length = gcd(len(str1), len(str2))
        # return str1[:gcd_length]

        if len(str1) == len(str2):
            return str1

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])