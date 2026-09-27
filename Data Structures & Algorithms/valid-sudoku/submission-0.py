class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 - pass solution 

        # check rows
        for r in range(9):
            visited = set()
            for i in range(9):
                if board[r][i] != "." and board[r][i] in visited:
                    return False
                visited.add(board[r][i])
        
        # check columns
        for c in range(9):
            visited = set()
            for i in range(9):
                if board[i][c] != "." and board[i][c] in visited:
                    return False
                visited.add(board[i][c])
        
        # check squares
        for s in range(9):
            visited = set()
            for i in range(3):
                for j in range(3):
                    piece = board[(s//3) * 3 + i][(s%3) * 3 + j]
                    if piece != "." and piece in visited:
                        return False
                    visited.add(piece)
        
        return True
