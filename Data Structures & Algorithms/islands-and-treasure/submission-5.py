class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == INF:
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1

                