class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        seen = set()
        visited = set()
        order = []

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if crs in visited:
                return True

            seen.add(crs)
            for neighbor in premap[crs]:
                if not dfs(neighbor):
                    return False
            seen.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return order        
