class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (-freq, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res