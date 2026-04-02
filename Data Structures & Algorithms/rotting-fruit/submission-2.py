class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                        fresh -= 1
                        visited.add((r, c))
                        q.append((r, c))
            minutes += 1
        return minutes if fresh == 0 else -1