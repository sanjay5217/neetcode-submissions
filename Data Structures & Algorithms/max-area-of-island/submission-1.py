class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        max_area = 0

        def dfs(r: int, c: int) -> int:
            visited.add((r,c))
            area = 1

            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROW and \
                    0 <= nc < COL and \
                    grid[nr][nc] == 1 and \
                    (nr, nc) not in visited
                ):
                    area += dfs(nr, nc)

            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area        