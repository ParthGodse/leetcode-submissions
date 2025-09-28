class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        count = 0

        def dfs_traverse(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in seen:
                    seen.add(neighbor)
                    dfs_traverse(neighbor)

        for i in range(n):
            if i not in seen:
                count += 1
                seen.add(i)
                dfs_traverse(i)

        return count
