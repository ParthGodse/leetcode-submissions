class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxx = 0
        area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxx =max(area, maxx)

        return maxx