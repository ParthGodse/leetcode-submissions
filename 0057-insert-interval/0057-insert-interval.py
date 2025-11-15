class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # s2, e2 = newInterval[]
            last_start, last_end = merged[-1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged