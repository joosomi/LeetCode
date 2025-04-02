class Solution:
    def isHappy(self, n: int) -> bool:
        
        # number_set = set()
        
        # while n != 1 :
        #     res = 0
        #     for i in range(len(str(n))):
        #         res += int(str(n)[i])**2
            
        #     if res not in number_set:
        #         number_set.add(res)
        #         n = res
        #     else: 
        #         return False
        # return True

        # 플로이드의 토끼와 거북이 알고리즘 >> 

        def sum_of_square(n):
            result = 0

            while n > 0:
                digit = n % 10 
                result += digit**2
                n = n // 10 
            
            return result 

        slow = n
        fast = sum_of_square(n)

        # slow == fast -> 사이클이 감지됨 (무한 루프)
        # fast ==1 -> happy number
        while fast != 1 and slow != fast:
            slow = sum_of_square(slow)
            fast = sum_of_square(sum_of_square(fast))
        
        return fast == 1 