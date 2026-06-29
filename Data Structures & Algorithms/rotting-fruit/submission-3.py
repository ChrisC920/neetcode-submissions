class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = deque()
        time = 0
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        