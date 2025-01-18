class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        visited = [False]* (len(s))
        def dfs(idx):
            if idx == len(s):
                return True 
            
            if visited[idx]:
                return False
            
            visited[idx] = True
            for word in wordDict:
                if s[idx:].startswith(word):
                    if dfs(idx+len(word)):
                        return True

            return False
                    
        return dfs(0)


            
               
                    

        
