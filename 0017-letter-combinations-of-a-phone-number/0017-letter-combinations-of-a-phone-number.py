class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []

        def backtrack(start, curr):
            if len(curr) >= len(digits):
                res.append(curr[:])
                return

            for val in mapp[digits[start]]:
                backtrack(start + 1, curr + val)

        if digits:
            backtrack(0, "")

        return res 