class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(start, n):
                curr.append(i + 1)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res