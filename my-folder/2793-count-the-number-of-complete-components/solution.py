class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            nonlocal edge_count, node_count
            seen.add(node)
            node_count += 1
            for nei in adj[node]:
                edge_count += 1
                if nei not in seen:
                    dfs(nei)

        # parts = 0
        complete = 0
        for node in range(n):
            if node not in seen:
                # parts += 1
                edge_count = 0
                node_count = 0
                dfs(node)
                actual_edges = edge_count // 2
                expected_edges = (node_count * (node_count - 1)) // 2
                if actual_edges == expected_edges:
                    complete += 1

        return complete
