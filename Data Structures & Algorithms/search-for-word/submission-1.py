class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()

        def backtrack(row: int, col: int, index: int) -> None:
            if index == len(word) - 1:
                return board[row][col] == word[index]

            if board[row][col] == word[index]:
                used.add((row, col))
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < len(board) and \
                        0 <= nc < len(board[0]) and \
                        (nr, nc) not in used:
                        if backtrack(nr, nc, index + 1):
                            return True
                used.remove((row, col))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True 
        return False
                        
