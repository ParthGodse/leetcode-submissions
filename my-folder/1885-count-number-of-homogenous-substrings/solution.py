class Solution:
    def countHomogenous(self, s: str) -> int:
        # MOD = 10**9 + 7
        # left = 0
        # res = 0

        # for right in range(len(s)):
        #     if s[left] == s[right]:
        #         res += right - left + 1
        #     else:
        #         res += 1
        #         left = right
        # return res % MOD
        MOD = 10**9 + 7
        res = 0
        count = 1  # count of consecutive identical characters

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res += count * (count + 1) // 2
                count = 1  # reset for new group

        # Add the last group
        res += count * (count + 1) // 2

        return res % MOD
