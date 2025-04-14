from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # good triplets (arr[i], arr[j], arr[k])
        # 0 <= i < j < k < arr.length
        #  |arr[i] - arr[j]| <= a
        #  |arr[j] - arr[k]| <= b
        #  |arr[k] - arr[i]| <= c
        # 절대값 - abs()
        # return the number of good triplets 
        
        cnt = 0

        for i, j, k in combinations(range(len(arr)), 3):
            if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[k]- arr[i]) <= c:
                cnt +=1 

        return cnt 