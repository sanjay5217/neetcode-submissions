class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            x, y = queue.popleft()
            for offset_x, offset_y in directions:
                if 0 <= x + offset_x < len(grid) and \
                    0 <= y + offset_y < len(grid[0]) and \
                    grid[x + offset_x][y + offset_y] == 2147483647:
                        queue.append((x + offset_x, y + offset_y))
                        grid[x + offset_x][y + offset_y] = grid[x][y] + 1

                