class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(s, openc, closec):
            if len(s) == 2*n:
                output.append(s)
                return
            
            if openc < n:
                backtrack(s + '(', openc + 1, closec)

            if closec < openc:
                backtrack(s + ')', openc, closec + 1)

        backtrack("", 0, 0)
        return output       
