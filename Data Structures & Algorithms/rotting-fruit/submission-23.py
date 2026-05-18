class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # consts
        MAX_X = len(grid)
        MAX_Y = len(grid[0])
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        # collect rotten Orange coords and put into stack
        queue = collections.deque()
        freshCount = 0
        for i in range(MAX_X):
            for j in range(MAX_Y):
                if grid[i][j] == FRESH:
                    freshCount += 1
                elif grid[i][j] == ROTTEN:
                    queue.append([i, j])

        # early-out
        if freshCount == 0:
            return 0

        # keep track of generations/minutes
        minutes = 0

        # util for checking adjacent fresh Orange
        def isValidCoordForRotting(x: int, y: int) -> bool:
            return x >= 0 and x < MAX_X and y >= 0 and y < MAX_Y and grid[x][y] == FRESH

        # simulate rotting of adjacent Oranges
        while freshCount > 0 and len(queue) > 0:
            generationCount = len(queue)
            for _ in range(generationCount):
                rottenOrangeCoord = queue.popleft()
                x, y = rottenOrangeCoord[0], rottenOrangeCoord[1]

                # up
                if isValidCoordForRotting(x - 1, y):
                    grid[x - 1][y] = ROTTEN
                    queue.append([x - 1, y])
                    freshCount -= 1

                # down 
                if isValidCoordForRotting(x + 1, y):
                    grid[x + 1][y] = ROTTEN
                    queue.append([x + 1, y])
                    freshCount -= 1

                # left
                if isValidCoordForRotting(x, y - 1):
                    grid[x][y - 1] = ROTTEN
                    queue.append([x, y - 1])
                    freshCount -= 1

                # right
                if isValidCoordForRotting(x, y + 1):
                    grid[x][y + 1] = ROTTEN
                    queue.append([x, y + 1])
                    freshCount -= 1
            
            minutes += 1

        # check for invalid state
        if freshCount > 0:
            return -1

        return minutes