import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones[0], stones[1])
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if y != x:
                new_stone = - (abs(y) - abs(x))
                heapq.heappush(stones, new_stone)

        if stones:
            return -stones[0]
        else:
            return 0