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
        print(cnt.items())

        for val, freq in cnt.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, val))
            
            elif freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, val))

        print(heap)
        return [ val for freq, val in heap ]