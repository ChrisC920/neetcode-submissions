import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
            return
        if num > self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.large) > len(self.small):
            v = heapq.heappop(self.large)
            heapq.heappush(self.small, -v)
        elif len(self.small) > len(self.large) + 1:
            v = heapq.heappop(self.small)
            heapq.heappush(self.large, -v)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
        
        