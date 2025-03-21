import heapq

class KthLargest:
    # 지원자 시험 점수 - k번째로 높은 점수 실시간 추적 

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        heap = nums[-self.k:]
        self.heap = heap
        heapq.heapify(heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
            
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)