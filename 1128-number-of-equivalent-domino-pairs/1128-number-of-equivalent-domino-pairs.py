class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:


        new = defaultdict(int)
        

        for i in dominoes:
            new[tuple(sorted(i))] += 1

        ans = 0
        for cnt in new.values():
            if cnt > 1:
                ans += cnt * (cnt-1) // 2 

        return ans 
        