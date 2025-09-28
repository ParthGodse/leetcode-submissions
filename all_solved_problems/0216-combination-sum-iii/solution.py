class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr, total):
            if len(curr) == k:
                if total == n:
                    res.append(curr[:])
                return

            for i in range(start, 10):
                if total + i > n:
                    break
                curr.append(i)
                backtrack(i + 1, curr, total + i)
                curr.pop()

        backtrack(1, [], 0)
        return res
