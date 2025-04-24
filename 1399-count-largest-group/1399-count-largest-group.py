class Solution:
    def countLargestGroup(self, n: int) -> int:
        # return the number of groups - 가장 큰 사이즈 
        
        g_size = defaultdict(int)

        
        for num in range(1, n+1):
            
            str_num = str(num)
            add = 0

            for i in range(len(str_num)):
                add += int(str_num[i])
            
            g_size[add] += 1
        
        max_val = max(g_size.values())
        
        ans = list(g_size.values()).count(max_val)
        return ans 
        

