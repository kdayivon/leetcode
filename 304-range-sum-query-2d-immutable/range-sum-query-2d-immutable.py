class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        self.preSum = [[0] * self.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                self.preSum[i][j] = self.matrix[i][j]
                if (i > 0): self.preSum[i][j] += self.preSum[i-1][j]
                if (j > 0): self.preSum[i][j] += self.preSum[i][j-1]
                if (i > 0) and (j > 0): 
                    self.preSum[i][j] -= self.preSum[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.preSum[row2][col2]
        if (row1 > 0): total -= self.preSum[row1 - 1][col2]
        if (col1 > 0): total -= self.preSum[row2][col1 - 1]
        if (row1 > 0) and (col1 > 0): total += self.preSum[row1 - 1][col1 - 1]
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)