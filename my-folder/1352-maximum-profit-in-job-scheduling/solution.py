class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        # ends = [job[1] for job in jobs]

        # n = len(jobs)

        # dp = [0] * (n + 1)

        # for i in range(1, n + 1):
        #     s, e, p = jobs[i - 1]

        #     j = bisect_right(ends, s)

        #     dp[i] = max(dp[i - 1], dp[j] + p)

        # return dp[n]

        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)
            j = i + 1

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))

            return res

        return dfs(0)
