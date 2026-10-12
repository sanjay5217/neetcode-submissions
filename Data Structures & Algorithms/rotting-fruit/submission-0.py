class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # Address empty case
        ROW, COL = len(grid), len(grid[0])
        
        queue = deque()
        fresh = 0

        # initialize the graph
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
                    
        if fresh == 0:
            return 0

        res = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                # length - start of minute 0
                x, y = queue.popleft()
                # perform a BFS
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy	
                    if (0 <= nx < ROW) and (0 <= ny < COL) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            res += 1

        # determine if every orange is rotten or not
        if fresh > 0:
            return -1
        return res	
