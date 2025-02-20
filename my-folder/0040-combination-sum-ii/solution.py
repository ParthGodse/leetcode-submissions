class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, curr, summ):
            if summ == target:
                res.append(curr[:])
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if summ + candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(i + 1, curr, summ + candidates[i])
                    curr.pop()

        backtrack(0, [], 0)
        return res
