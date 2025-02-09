class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        ## dp => s의 인덱스 i부터 끝까지 단어 분해가 가능한가?
        
        dp = [None] * (len(s))

        def dfs(idx):
            if idx == len(s):  
                return True
            if dp[idx] is not None:
                return dp[idx]
            
            for i in range(idx+1, len(s)+1):
                if s[idx:i] in wordDict:
                    dp[idx] = True
                    if dfs(i) is True:
                        return True
            dp[idx]= False
            return False
        
        return dfs(0)

        

