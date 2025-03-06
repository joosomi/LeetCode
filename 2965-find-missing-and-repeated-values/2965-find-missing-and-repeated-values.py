class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)

        ans = []
        cnt = {}
        for i in range(n*n):
            cnt[i+1] = 0


        for i in range(n):
            for j in range(n):
                if cnt[grid[i][j]] == 0:
                    cnt[grid[i][j]] +=1
                elif cnt[grid[i][j]] == 1:
                    cnt[grid[i][j]] +=1
                    ans.append(grid[i][j])
        print(ans)
        print(cnt)
        for i in range(n*n):
            print(cnt[i+1])
            if cnt[i+1] == 0:
                ans.append(i+1)
        return ans
                    
            