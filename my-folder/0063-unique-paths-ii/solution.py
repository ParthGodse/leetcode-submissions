class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols

        if obstacleGrid[-1][-1] == 0:
            dp[-1] = 1
        else:
            dp[-1] = 0

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col + 1 < cols:
                    dp[col] += dp[col + 1]

        return dp[0]
