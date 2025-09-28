class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        adj = {i:[] for i in range(n)}

        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))

        def dfs(node):
            visited.add(node)
            count = 0
            for nei, forward in adj[node]:
                if nei not in visited:
                    count += forward
                    count += dfs(nei)

            return count

        return dfs(0)
