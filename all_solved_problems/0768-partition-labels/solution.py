class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {char: idx for idx, char in enumerate(s)}
        partitions = []
        start, end = 0, 0

        for idx, char in enumerate(s):
            end = max(end, last_occur[char])
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1

        return partitions
