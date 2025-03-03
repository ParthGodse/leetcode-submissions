class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0

        prevend = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     start, end = intervals[i]
        for start, end in intervals[1:]: 
            if start >= prevend:
                prevend = end
            else:
                count += 1
                prevend = min(prevend, end)

        return count
