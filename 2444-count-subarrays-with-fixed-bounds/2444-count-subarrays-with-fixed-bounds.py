class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # fixed-bound subarray
        # - 최소값 -> minK
        # - 최대값 -> maxK
        # fixed-bound subarrays의 개수 리턴


        arrs = []
        start = 0
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                if start < i:
                    arrs.append(nums[start:i])
                start = i + 1
        
        if start < len(nums):
            arrs.append(nums[start:])
            
        print(arrs)

        ans = 0

        for arr in arrs:
            min_pos, max_pos = -1, -1

            for i in range(len(arr)):
                if arr[i] == minK:
                    min_pos = i
                if arr[i] == maxK:
                    max_pos = i
                bound = min(min_pos, max_pos) # 시작점의 후보
                if bound != -1:
                    ans += bound + 1 
                
        
        return ans 