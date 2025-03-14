class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 각 더미는 하위 더미로 나눌 수 있지만,
        # 2개의 더미를 합칠 수는 없다. 

        # K명의 아이들
        # - 각 아이가 동일한 개수의 사탕을 받을 수 있도록
        # - 각 아이는 오직 하나의 더미에서만 사탕을 받을 수 있음.
        # - 각 아이가 받을 수 있는 최대 사탕 개수 반환 

        candies.sort()

        left= 1
        right = max(candies)
        
        while left <= right :
            mid = (left+ right) //2 
            cnt = 0
            
            for i in range(len(candies)):
                cnt += candies[i] // mid
            
            if k <= cnt:
                left = mid + 1
            else:
                right = mid -1 

       
        return right
