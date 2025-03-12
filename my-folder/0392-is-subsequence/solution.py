class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0

        # if not s:
        #     return True

        # while j < len(t):
        #     if i < len(s) and s[i] == t[j]:
        #         i += 1
        #     j += 1

        #     if i == len(s):
        #         return True
        # return False 
        if not s:
            return True
        correct = len(s)
        i = 0
        for letter in t:
            if s[i] == letter:
                i += 1
            if i == correct:
                return True
        return False
