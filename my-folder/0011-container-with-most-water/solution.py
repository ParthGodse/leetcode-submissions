class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        i, j = 0, n - 1

        while i < j:
            diff = j - i 
            mini = min(height[i], height[j])
            area = diff * mini

            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
