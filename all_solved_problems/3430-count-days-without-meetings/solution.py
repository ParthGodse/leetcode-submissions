class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = [meetings[0]]

        for i in range(1, len(meetings)):
            start, end = meetings[i]
            last_start, last_end = merged[-1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        # unused_count = 0

        # if merged[0][0] > 1:
        #     unused_count += merged[0][0] - 1

        # for i in range(len(merged) - 1):
        #     gap = merged[i + 1][0] - merged[i][1] - 1
        #     if gap > 0:
        #         unused_count += gap

        # if merged[-1][1] < days:
        #     unused_count += days - merged[-1][1]

        # return unused_count
        count = 0
        for start, end in merged:
            count += end - start + 1

        return days - count
