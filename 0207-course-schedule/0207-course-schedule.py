class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs in seen:
                return False

            if adj[crs] == []:
                return True

            seen.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            seen.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True