class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                break
            row = i

        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            p = l + ((r - l) // 2)
            if matrix[row][p] < target:
                l = p + 1
            elif matrix[row][p] > target:
                r = p - 1
            else:
                return True

        return False
