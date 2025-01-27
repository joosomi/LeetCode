class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 컨테이너가 담을 수 있는 물의 최대 양
        # 2개의 x 축을 활용해아 함
        
        

        left = 0
        right = len(height)-1
        rectangles = []

        while left < right:
            rectangle = (right - left) * min(height[left], height[right])
            rectangles.append(rectangle)

            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1

            
            new_rac = (right - left) * min(height[left], height[right])
            print(new_rac, right, left, height[left], height[right])

            rectangles.append(max(rectangle, new_rac))
        
        return max(rectangles)
        
            
            

         
            


