class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            size = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    size += 1
                    visited.add((nr, nc))
                    q.append((nr, nc))
            return size
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res