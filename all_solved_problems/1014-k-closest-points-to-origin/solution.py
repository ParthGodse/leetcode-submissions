class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i, j in points:
            dist = ((i)**2 + (j)**2)
            min_heap.append([dist, i, j])
        heapq.heapify(min_heap)
        res = []
        for _ in range(k):
            [_, x, y] = heapq.heappop(min_heap)
            res.append([x, y])

        return res
