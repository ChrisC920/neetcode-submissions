import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 1:
            return list(reversed(heapq.nsmallest(len(self.heap) // 2 + 1, self.heap)))[0]
        else:
            mL = list(reversed(heapq.nsmallest(len(self.heap) // 2 + 1, self.heap)))
            return (mL[0] + mL[1]) / 2.0