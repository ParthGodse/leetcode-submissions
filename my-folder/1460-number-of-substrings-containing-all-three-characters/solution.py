class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            char[s[right]] += 1

            while char['a'] > 0 and char['b'] > 0 and char['c'] > 0:
                count  += len(s) - right
                char[s[left]] -= 1
                left += 1
        return count
