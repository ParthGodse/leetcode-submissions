class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l = 0
        r = 0
        count = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                count += 1
                l += 1
                r += 1
            else:
                r += 1
            if count == len(s):
                return True
        return False