class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        count = 0

        for char in range(len(s)):
            while s[char] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[char])

            count = max(count, char - l + 1)
        return count
