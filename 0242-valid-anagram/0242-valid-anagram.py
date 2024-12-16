class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        lst_s = sorted(list(s))
        lst_t = sorted(list(t))


        if lst_s == lst_t:
            return True
        return False