class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x: int, y: int) -> float:
            return math.sqrt(x**2 + y**2)
        
        heap = []
        for point in points:
            x, y = point[0], point[1]
            heapq.heappush(heap, (dist(x, y), [x, y]))
        
        res = []
        for i in range(k):
            d, p = heapq.heappop(heap)
            res.append(p)
        return res
        
