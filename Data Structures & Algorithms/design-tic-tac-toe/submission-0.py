class TicTacToe:

    def __init__(self, n: int):
        self.boardSize = n
        self.board = [[0 for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        self.winner = 0

    def move(self, row: int, col: int, player: int) -> int:
        if self.winner != 0:
            return self.winner

        self.board[row][col] = player

        # row check
        rowWin = True
        for i in range(self.boardSize):
            if self.board[i][col] != player:
                rowWin = False
                break

        if rowWin:
            self.winner = player
            return self.winner

        # col check
        colWin = True
        for i in range(self.boardSize):
            if self.board[row][i] != player:
                colWin = False
                break

        if colWin:
            self.winner = player
            return self.winner

        # diagCheck
        diagWin = True
        if row == col:
            for i in range(self.boardSize):
                if self.board[i][i] != player:
                    diagWin = False
                    break
        else:
            diagWin = False

        if diagWin:
            self.winner = player
            return self.winner
            
        counterDiagWin = True
        if row == self.boardSize - col - 1:
            for i in range(self.boardSize):
                if self.board[i][self.boardSize - i - 1] != player:
                    counterDiagWin = False
                    break
        else:
            counterDiagWin = False

        if counterDiagWin:
            self.winner = player
            return self.winner

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
