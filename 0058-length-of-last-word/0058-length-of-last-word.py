class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                while s[i] != " " and i >= 0:
                    count += 1
                    i -= 1
                return count 