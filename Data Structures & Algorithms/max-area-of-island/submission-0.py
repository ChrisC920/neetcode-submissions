class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c) -> int:
            island_size = 1
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
                        island_size += 1
            return island_size

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    size = bfs(r, c)
                    max_area = max(max_area, size)
        return max_area