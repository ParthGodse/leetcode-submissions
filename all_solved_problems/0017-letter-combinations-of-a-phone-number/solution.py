class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def backtrack(i, curr):
            if i == len(digits):
                res.append("".join(curr))
                return

            curr_digit = digits[i]
            for j in mapping[curr_digit]:
                curr.append(j)
                backtrack(i + 1, curr)
                curr.pop()

        res = []
        backtrack(0, [])
        return res
