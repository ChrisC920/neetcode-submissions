class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] == "0":
                        continue
                    
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res