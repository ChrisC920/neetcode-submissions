import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        max_heap = []
        for val, freq in counter.items():
            heapq.heappush(max_heap, (-freq, val))
        

        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res