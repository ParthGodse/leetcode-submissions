class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            x, y = questions[i]
            next_ = i + y + 1

            dp[i] = x + (dp[next_] if next_ < n else 0)

            if i < n - 1:
                dp[i] = max(dp[i], dp[i + 1])

        return dp[0] 
