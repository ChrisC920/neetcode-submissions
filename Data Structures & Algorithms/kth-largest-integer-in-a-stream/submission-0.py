class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return self.heap[-self.k]