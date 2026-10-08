class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        count = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count+=1
                    visited.add((r,c))
                    stack = [(r, c)]
                    
                    while stack:
                        x, y = stack.pop()
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nr, nc = x + dr, y + dc
                            if 0 <= nr < ROW and 0 <= nc < COL and \
                                grid[nr][nc] == "1" and \
                                (nr, nc) not in visited:
                                visited.add((nr, nc))
                                stack.append((nr, nc))
        
        return count
