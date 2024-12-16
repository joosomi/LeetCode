import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
        sorted_cnt = sorted(cnt.keys(), key=lambda x: cnt[x], reverse= True)

        heap = []
        for i in range(len(sorted_cnt)):
            heapq.heappush(heap, sorted_cnt[i])
            if len(heap) == k:
                return heap        


        

