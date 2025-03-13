class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)

        seen = set()
        for value in freq.values():
            if value in seen:
                return False
            seen.add(value)
        return True
