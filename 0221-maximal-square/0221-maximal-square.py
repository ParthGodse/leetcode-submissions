class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {}

        def helper(i, j):
            if i >= rows or j >= cols:
                return 0

            if (i, j) not in dp:
                down = helper(i + 1, j)
                right = helper(i, j + 1)
                diag = helper(i + 1, j + 1)

                dp[(i, j)] = 0

                if matrix[i][j] == "1":
                    dp[(i, j)] = 1 + min(down, right, diag)

            return dp[(i, j)]
        helper(0, 0)
        return max(dp.values()) ** 2