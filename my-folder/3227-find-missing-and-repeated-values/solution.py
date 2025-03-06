class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        ans = []

        for i in range(n):
            for j in range(n):
                num = grid[i][j]

                if num in seen:
                    ans.append(num)
                else:
                    seen.add(num)

        for num in range(1, n * n + 1):
            if num not in seen:
                ans.append(num)

        return ans
