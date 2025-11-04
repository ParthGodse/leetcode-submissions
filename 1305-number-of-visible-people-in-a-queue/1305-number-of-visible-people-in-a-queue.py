class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)

        res = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            height = heights[i]

            visible = 0

            while stack and height > stack[-1]:
                visible += 1
                stack.pop()

            if stack:
                visible += 1
            
            res[i] = visible
            stack.append(height)
        return res