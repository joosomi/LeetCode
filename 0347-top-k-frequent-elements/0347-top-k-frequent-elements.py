class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        cnt = Counter(nums)
        cnt = sorted(cnt, key=lambda x: cnt[x], reverse = True)
      
        return cnt[:k]


