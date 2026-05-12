class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows and cols
        for i in range(9):
            usedRows = [False] * 9
            usedCols = [False] * 9
            for j in range(9):
                if board[i][j].isnumeric():
                    value = int(board[i][j]) - 1
                    if usedRows[value]:
                        return False
                    usedRows[value] = True
                if board[j][i].isnumeric():
                    value = int(board[j][i]) - 1
                    if usedCols[value]:
                        return False
                    usedCols[value] = True

        # cells
        for p in range(0, 9, 3):
            for q in range(0, 9, 3):
                usedCells = [False] * 9
                for i in range(3):
                    for j in range(3):
                        x = p + i
                        y = q + j
                        if board[x][y].isnumeric():
                            value = int(board[x][y]) - 1
                            if usedCells[value]:
                                return False
                            usedCells[value] = True

        return True