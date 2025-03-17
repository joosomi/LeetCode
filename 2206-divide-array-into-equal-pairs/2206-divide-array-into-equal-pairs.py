class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        cnt = Counter(nums)

        print(cnt)

        for idx, count in cnt.items():
            if count % 2 != 0:
                return False
        return True
