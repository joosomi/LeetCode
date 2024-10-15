class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
       
        # cnt = [arr.count(i) for i in arr] 
        # print(cnt)
        # if len(set(arr)) == len(set(cnt)):
        #     return True
        # else:
        #     return False


        # Solution 2.
        cnt = {}
        for i in arr:
            cnt[i] = cnt.get(i, 0) + 1  # 값이 없으면 0반환 
        return len(cnt) == len(set(cnt.values()))