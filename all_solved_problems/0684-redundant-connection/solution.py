class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(u, v) for u, v in edges) + 1
        adj = {i:[] for i in range(n)}

        def dfs(node, parent):
            if node in seen:
                return True

            seen.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in seen or dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            seen = set()
            adj[u].append(v)
            adj[v].append(u)
            if dfs(u, -1):
                return [u, v]
        return [] 
