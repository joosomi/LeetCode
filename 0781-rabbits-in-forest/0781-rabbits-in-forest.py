class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        cnt = Counter(answers)

        ans = 0
        zero = 0
        
        print(cnt)
        for key, val in cnt.items():
            if key > 0:
                ans += ceil(val / (key + 1)) * (key + 1)
            elif key == 0:
                ans += val 
                
        
        return ans 