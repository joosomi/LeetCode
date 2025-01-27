class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [-1] * (len(s)+1)
        dp[0] = True

        def dfs(idx):
            if len(s) == idx:
                return True
            
            if dp[idx] != -1:
                return dp[idx]

            for char in wordDict:
                if s[idx:idx+len(char)]== char:
                    if dfs(idx + len(char)):
                        dp[idx + len(char)] = True

            dp[idx] = False

        return dp[len(s)]