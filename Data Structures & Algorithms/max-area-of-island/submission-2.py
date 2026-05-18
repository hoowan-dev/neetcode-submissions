class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # constants
        WATER = 0
        LAND = 1
        VISITED = 2
        MAX_X, MAX_Y = len(grid), len(grid[0])

        def floodFill(currX: int, currY: int) -> int:
            def isValid(x: int, y: int) -> bool:
                return x >= 0 and x < MAX_X and y >= 0 and y < MAX_Y and grid[x][y] == LAND

            grid[currX][currY] = VISITED

            upRes = floodFill(currX - 1, currY) if isValid(currX - 1, currY) else 0
            downRes = floodFill(currX + 1, currY) if isValid(currX + 1, currY) else 0
            leftRes = floodFill(currX, currY - 1) if isValid(currX, currY - 1) else 0
            rightRes = floodFill(currX, currY + 1) if isValid(currX, currY + 1) else 0

            return upRes + downRes + leftRes + rightRes + 1

        maxArea = 0
        for i in range(MAX_X):
            for j in range(MAX_Y):
                if grid[i][j] == LAND:
                    maxArea = max(maxArea, floodFill(i, j))

        return maxArea