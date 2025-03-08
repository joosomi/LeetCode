class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left, right = 0, k-1
        ans = 0

        if "B"*k in blocks:
            return 0

        while right < n:

            cnt = blocks[left:right+1].count("B")
    
            if ans == 0:
                ans = k-cnt
            else:
                ans = min(ans, k-cnt)

            left += 1
            right +=1 

        return ans