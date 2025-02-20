class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(start, curr, summ):
            if summ == target:
                res.append(curr[:])
                return

            for i in range(start, n):
                if summ + candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(i, curr, summ + candidates[i])
                    curr.pop()

        backtrack(0, [], 0)
        return res
