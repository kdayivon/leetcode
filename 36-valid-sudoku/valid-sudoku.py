class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board[0])
        for i in range(n):  # rows
            row_set = set()
            for num in range(n):
                if board[i][num] == ".":
                    continue
                if board[i][num]in row_set:
                    return False
                row_set.add(board[i][num])
                    
        for j in range(n):  # cols
            col_set = set()
            for num in range(n):
                if board[num][j] == ".":
                    continue
                if board[num][j] in col_set:
                    return False
                col_set.add(board[num][j])
                    
        for k in range(n):  # boxs
            box_set = set()
            for a in range(3):
                for b in range(3):
                    row = (k // 3) * 3 + a
                    col = (k % 3) * 3 + b
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in box_set:
                        return False
                    box_set.add(board[row][col])
        return True
