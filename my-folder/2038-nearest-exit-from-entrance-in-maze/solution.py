class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, steps = q.popleft()

            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and [r, c] != entrance:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == '.':
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))

        return -1
