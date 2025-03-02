class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if not intervals:
        #     return [newInterval]

        # intervals.append(newInterval)
        # intervals.sort()
        # merged = [intervals[0]]

        # for i in range(1, len(intervals)):
        #     start, end = intervals[i]
        #     last_start, last_end = merged[-1]

        #     if start <= last_end:
        #         merged[-1][1] = max(last_end, end)
        #     else:
        #         merged.append([start, end])

        # return merged
        i = 0
        n = len(intervals)

        # Find the correct insert position
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1

        # Merge overlapping intervals directly in the list
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            intervals.pop(i)  # Remove merged interval
            n -= 1  # Decrease size since we removed an element

        # Insert the merged interval at the correct position
        intervals.insert(i, newInterval)

        return intervals  # Returning modified intervals for clarity
