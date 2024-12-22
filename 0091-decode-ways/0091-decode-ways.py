class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == "0":
            return 0

        ans = 0

        length = len(s)
        print(length)
        dp = [0]*(length + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, length+1):
            #한 자리 숫자가 하나의 알파벳
            if 1<= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            # 두 자리 숫자가 하나의 알파벳으로 유효한 경우 
            if 10 <= int(s[i-2:i]) <=26:
                dp[i] += dp[i-2]
        
        print(dp)
        return dp[length]
