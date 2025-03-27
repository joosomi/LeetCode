class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left, right = 0, len(s)-1


        while left <= right:
            val_l = s[left]
            val_r = s[right]
            s[left], s[right] = val_r, val_l
            left += 1
            right -=1

        return s