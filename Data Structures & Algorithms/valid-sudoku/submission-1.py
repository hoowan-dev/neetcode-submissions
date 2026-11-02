class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # grid checks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                found = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != '.':
                            if board[m][n] in found:
                                return False
                            found.add(board[m][n])


        # horizontal and vertical checks
        for i in range(9):
            foundHor = set()
            foundVer = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in foundHor:
                        print("b")
                        return False
                    foundHor.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in foundVer:
                        print("c")
                        return False
                    foundVer.add(board[j][i])

        return True
