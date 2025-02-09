class Solution:
    def maxArea(self, height: List[int]) -> int:
         
        left, right = 0, len(height) -1
        max_water = 0

        while left < right:      
            current = (right - left) * min(height[right], height[left])
            max_water = max(current, max_water)

            if height[left] < height[right]:
                left +=1 
            else:
                right -= 1
            


        return max_water