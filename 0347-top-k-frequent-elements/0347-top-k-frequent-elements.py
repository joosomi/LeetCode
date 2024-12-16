import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
       

        heap = []
        for val, freq in cnt.items():
            heapq.heappush(heap, (freq, val))

            if len(heap) > k:
                heapq.heappop(heap)

        return [val for freq, val in heap]

        

