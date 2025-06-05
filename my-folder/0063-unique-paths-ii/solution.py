class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        if obstacleGrid[-1][-1] == 0:
            dp[-1] = 1
        else:
            dp[-1] = 0

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col + 1 < n:
                    dp[col] += dp[col + 1]

        return dp[0]
