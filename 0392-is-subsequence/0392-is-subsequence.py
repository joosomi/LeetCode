class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # iter()를 사용하여 t의 문자들을 순차적으로 확인
        t_iter = iter(t)
        
        # s의 각 문자가 t_iter에서 순차적으로 나타나는지 확인
        return all(i in t_iter for i in s)
        