class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and board[r][c] == 'O':
                        visited.add((r, c))
                        q.append((r, c))
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][COLS - 1] == 'O':
                bfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[ROWS - 1][c] == 'O':
                bfs(ROWS - 1, c)
        
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'





