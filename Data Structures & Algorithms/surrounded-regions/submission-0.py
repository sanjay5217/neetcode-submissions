class DSU:
    parent: list[int]
    rank: list[int]

    def __init__(self) -> None:
        self.parent = []
        self.rank = []

    def make(self, item: int) -> None:
        self.parent.append(item)
        self.rank.append(0)
    
    def find(self, target: int) -> int:
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]
    
    def union(self, target_1: int, target_2: int) -> bool:
        rep1, rep2 = self.find(target_1), self.find(target_2)
        if rep1 == rep2:
            return False
        
        if self.rank[rep2] <= self.rank[rep1]:
            self.parent[rep2] = rep1
            if self.rank[rep2] == self.rank[rep1]:
                self.rank[rep1] += 1
        else:
            self.parent[rep1] = rep2
        
        return True
    def connection(self, target_1: int, target_2: int) -> bool:
        return self.find(target_1) == self.find(target_2)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # row 1: col 0, 1, 2, 3 -> 4, 5, 6, 7
        # (row * 4) + col for linear grid
        ROW, COL = len(board), len(board[0])
        dsu = DSU()

        for item in range(ROW*COL+1):
            dsu.make(item)

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] != "O":
                    continue
                if (col == 0 or col == COL-1 or row == 0 or row == ROW-1):
                    dsu.union(ROW*COL, (COL*row) + col)
                else:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = row + dx, col + dy
                        if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == "O":
                            dsu.union(row * COL + col, nr * COL + nc)

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == "O" and not dsu.connection(ROW * COL, row*COL + col):
                    board[row][col] = "X"






