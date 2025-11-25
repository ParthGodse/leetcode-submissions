class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)

        if self.minheap and self.maxheap and self.minheap[0] < (-1 * self.maxheap[0]):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1*val)

        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1*val)

        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]

        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]

        return ((-1*self.maxheap[0]) + self.minheap[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()