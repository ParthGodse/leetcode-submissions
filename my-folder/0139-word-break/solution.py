# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # max_len = max(map(len, wordDict))

        # for i in range(1, n + 1):
        #     for j in range(i - 1, max(i - max_len - 1, -1), -1):
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             break
        # return dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False
