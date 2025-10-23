class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dp = [False] * (len(s) + 1)
        # dp[len(s)] = True

        # for i in range(len(s) - 1, -1, -1):
        #     for w in wordDict:
        #         if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
        #             dp[i] = dp[i + len(w)]
        #         if dp[i]:
        #             break

        # return dp[0]
        
        words = set(wordDict)
        q = deque([0])
        visit = set()
        while q:
            start = q.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in visit:
                    continue

                if s[start:end] in words:
                    q.append(end)
                    visit.add(end)

        return False   