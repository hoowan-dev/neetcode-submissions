class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_X = len(board)
        MAX_Y = len(board[0])
        
        def search(currCoord, targetIndex, prevCoords) -> bool:
            def isInBounds(coord):
                return coord[0] >= 0 and coord[0] < MAX_X and coord[1] >= 0 and coord[1] < MAX_Y
            def shouldSearch(coord):
                return coord not in prevCoords and isInBounds(coord) and board[coord[0]][coord[1]] == word[targetIndex]

            if targetIndex == len(word):
                return True

            targetChar = word[targetIndex]
            found = False

            up = (currCoord[0] - 1, currCoord[1])
            if shouldSearch(up):
                prevCoords.add(up)
                found = found or search(up, targetIndex + 1, prevCoords)
                prevCoords.remove(up)

            down = (currCoord[0] + 1, currCoord[1])
            if shouldSearch(down):
                prevCoords.add(down)
                found = found or search(down, targetIndex + 1, prevCoords)
                prevCoords.remove(down)

            left = (currCoord[0], currCoord[1] - 1)
            if shouldSearch(left):
                prevCoords.add(left)
                found = found or search(left, targetIndex + 1, prevCoords)
                prevCoords.remove(left)

            right = (currCoord[0], currCoord[1] + 1)
            if shouldSearch(right):
                prevCoords.add(right)
                found = found or search(right, targetIndex + 1, prevCoords)
                prevCoords.remove(right)

            return found

        for i in range(MAX_X):
            for j in range(MAX_Y):
                if board[i][j] == word[0] and search((i,j), 1, { (i,j) }):
                    return True

        return False