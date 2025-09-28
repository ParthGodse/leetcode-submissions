class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        seen = set()

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if premap[crs] == []:
                return True

            seen.add(crs)
            for neighbor in premap[crs]:
                if not dfs(neighbor):
                    return False
            seen.remove(crs)
            premap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
