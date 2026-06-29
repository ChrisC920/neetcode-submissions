class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def bfs(r, c):
            q = deque()
            visited = set()
            visited.add((r, c))
            q.append((r, c))
            dist = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return dist
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if not (0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] == -1 or (nr, nc) in visited:
                            continue
                        q.append((nr, nc))
                        visited.add((nr, nc))
                dist += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)