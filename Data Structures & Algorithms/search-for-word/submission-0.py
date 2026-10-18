class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        
        def backtrack(row: int, col: int, word: str) -> bool:
            # Termination state
            if len(word) == 1:
                return board[row][col] == word
            
            if board[row][col] == word[0]:
                used.add((row, col))
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= row + dr < len(board) and \
                        0 <= col + dc < len(board[0]) and \
                        (row + dr, col + dc) not in used:
                        if backtrack(row + dr, col + dc, word[1:]):
                            return True
                used.remove((row, col))
            
            return False 
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, word):
                    return True
        return False

                        
