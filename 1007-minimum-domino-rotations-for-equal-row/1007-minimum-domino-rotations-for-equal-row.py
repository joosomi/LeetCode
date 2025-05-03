class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # tops or bottoms가 다 같아지게 되는 최소 회전 횟수 Return
        # 불가능하다면 Return -1 


        candidates = {tops[0], bottoms[0]}

        min_top_rot = float("inf")
        # top을 한 줄로
        for t in candidates:
            ta = 0
            for i in range(len(tops)):
                if tops[i] != t and bottoms[i] != t:
                    break
                elif tops[i] != t:
                    ta += 1
            else:
                min_top_rot = min(min_top_rot, ta)
            
      
        # bottoms을 한 줄로 
 
        min_bo_rot = float("inf")
        for b in candidates:
            ba = 0
            for i in range(len(tops)):
                if bottoms[i] != b and tops[i] != b:
                    break
                elif bottoms[i] != b:
                    ba += 1
            else:
                min_bo_rot = min(min_bo_rot, ba)
        
        return min(min_bo_rot, min_top_rot) if min(min_bo_rot, min_top_rot) != float("inf") else -1 