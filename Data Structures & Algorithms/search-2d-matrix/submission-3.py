class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if i + 1 < len(matrix) and matrix[i + 1][0] <= target:
                continue

            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                        return True

            return False
        
        return False