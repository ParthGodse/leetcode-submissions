class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])  
        res = 1
        prevEnd = points[0][1]

        for start, end in points[1:]:
            if start > prevEnd:
                res += 1
                prevEnd = end  

        return res

