class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Initializing a prefix sum matrix 
        # M[r][c] = M[r][c-1] + M[r-1][c] - M[r-1][c-1]

        self.p_matrix = []
        ROW, COL = len(matrix), len(matrix[0])
        for r in range(ROW):
            m_row = []
            for c in range(COL):
                value = matrix[r][c]
                if r > 0:
                    value += self.p_matrix[r-1][c]
                if c > 0:
                    value += m_row[-1]
                if r > 0 and c > 0:
                    value -= self.p_matrix[r-1][c-1]
                m_row.append(value)
            self.p_matrix.append(m_row)

        # Trace: 
        # [[3, 0, 1]
        #  [5, 6, 3]
        #  [1, 2, 0]]

        # p_matrix = [[3,3,4], [8, 14, 18], [9, 17, 21]]
        # m_row = [9, 17, 21]
        # r = 2
        # c = 2
        # value = 21

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        value = self.p_matrix[row2][col2]
        if row1 > 0:
            value -= self.p_matrix[row1-1][col2]
        if col1 > 0:
            value -= self.p_matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            value += self.p_matrix[row1-1][col1-1]
        return value 

        # Trace: 
        # [[3, 3, 4]
        #  [8, 14, 18]
        #  [9, 17, 21]]

        # sum(1, 1, 2, 2)
        # value = 21 - 18 - 17 + 14 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)