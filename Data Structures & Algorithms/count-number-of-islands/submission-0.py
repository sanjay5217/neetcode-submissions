class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        count = 0

        def dfs(r: int, c: int):
            visited.add((r,c))

            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROW and \
                    0 <= nc < COL and \
                    grid[nr][nc] == "1" and \
                    (nr, nc) not in visited
                ):
                    dfs(nr, nc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        
        return count
