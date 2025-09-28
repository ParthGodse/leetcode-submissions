class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0

        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            if count == 1:
                chars[j] = ch
                j += 1
            else:
                chars[j] = ch
                j += 1
                for digit in str(count):
                    chars[j] = digit
                    j += 1
        chars[:] = chars[:j]
        return j
