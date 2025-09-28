class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        # for round in range(t):
        #     nxt = [0] * 26
        #     nxt[0] = cnt[25]
        #     nxt[1] = (cnt[25] + cnt[0]) % mod
        #     for i in range(2, 26):
        #         nxt[i] = cnt[i - 1]
        #     cnt = nxt
        # ans = sum(cnt) % mod
        # return ans
        for _ in range(t):
            tmp = [0] * 26
            for i in range(26):
                if i == 25:
                    tmp[0] = (tmp[0] + cnt[i]) % mod
                    tmp[1] = (tmp[1] + cnt[i]) % mod
                else:
                    tmp[i + 1] = (tmp[i + 1] + cnt[i]) % mod
            cnt = tmp

        return sum(cnt) % mod
