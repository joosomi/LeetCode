class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        cnt = Counter(answers)

        ans = 0
        zero = 0
        
        for key, val in cnt.items():
            group_size = key + 1 
            if key > 0:
                ans += ceil(val/group_size) * group_size
            elif key == 0:
                ans += val 
                
        
        return ans 

