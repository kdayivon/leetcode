class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, (n * m) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            row = mid // m
            col = mid % m
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                left = mid + 1 
            elif (matrix[row][col] > target):
                right = mid - 1
        return False 
