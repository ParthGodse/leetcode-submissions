class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        rows, cols = len(board), len(board[0])

        def bfs(r, c):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = deque([(r, c)])
            board[r][c] = "S"
            
            while q:
                r, c  = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                        board[row][col] = "S"
                        q.append((row, col))

        for r in range(rows):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][cols-1] == 'O':
                bfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[rows-1][c] == 'O':
                bfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"

