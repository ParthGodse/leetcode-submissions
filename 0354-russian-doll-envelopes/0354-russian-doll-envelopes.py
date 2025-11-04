class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        heights = [h for _, h in envelopes]

        LIS = []

        for h in heights:
            pos = bisect.bisect_left(LIS, h)

            if pos == len(LIS):
                LIS.append(h)
            else:
                LIS[pos] = h

        return len(LIS)