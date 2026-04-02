class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x: int, y: int) -> float:
            return math.sqrt(x**2 + y**2)
        
        heap = []
        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(heap, (-dist(x, y), [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
        
