class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()

        minheap = [[grid[0][0], 0, 0]]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        visit.add((0, 0))

        while minheap:
            time, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in visit:
                    continue

                visit.add((neiR, neiC))
                heapq.heappush(minheap, [max(time, grid[neiR][neiC]), neiR, neiC])