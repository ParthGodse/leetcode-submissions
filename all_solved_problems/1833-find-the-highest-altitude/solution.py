class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0] + gain
        prefix = [0] * len(gain)
        prefix[0] = gain[0]

        for i in range(len(gain)):
            prefix[i] = prefix[i - 1] + gain[i]

        return max(prefix)
