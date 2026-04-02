class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            top = heapq.heappop(heap)
            top2 = heapq.heappop(heap)
            if top == top2:
                continue
            heapq.heappush(heap, top - top2)
        
        return 0 if len(heap) == 0 else -heap[0]