class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = [0] * 40
        max_c = 0

        for i in range(1, n + 1):
            digit = sum(int(c) for c in str(i))
            freq[digit] += 1
            max_c = max(max_c, freq[digit])

        return sum(1 for x in freq if x == max_c)


