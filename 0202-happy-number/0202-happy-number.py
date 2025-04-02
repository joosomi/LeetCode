class Solution:
    def isHappy(self, n: int) -> bool:
        
        number_set = set()
        
        while n != 1 :
            res = 0
            for i in range(len(str(n))):
                res += int(str(n)[i])**2
            
            if res not in number_set:
                number_set.add(res)
                n = res
            else: 
                return False
        return True

        

        