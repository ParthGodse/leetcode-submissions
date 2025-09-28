class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxheap = [[-count, char] for char, count in freq.items()]
        heapq.heapify(maxheap)

        prev = None
        res = ""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            count, char = heapq.heappop(maxheap)
            res += char
            count += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return res
