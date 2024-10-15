class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
       
        cnt = [arr.count(i) for i in arr] 
        print(cnt)
        if len(set(arr)) == len(set(cnt)):
            return True
        else:
            return False