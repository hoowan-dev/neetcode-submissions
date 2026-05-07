def floodFill(grid: List[List[int]], coord: (int, int)) -> None:
    # save current cost
    x, y = coord[0], coord[1]
    cost = grid[x][y]

    # up
    if (x - 1 >= 0) and (grid[x - 1][y] > cost):
        grid[x - 1][y] = cost + 1
        floodFill(grid, (x - 1, y))

    # down
    if (x + 1 < len(grid)) and (grid[x + 1][y] > cost):
        grid[x + 1][y] = cost + 1
        floodFill(grid, (x + 1, y))

    # left
    if (y - 1 >= 0) and (grid[x][y - 1] > cost):
        grid[x][y - 1] = cost + 1
        floodFill(grid, (x, y - 1))

    # right
    if (y + 1 < len(grid[x])) and (grid[x][y + 1] > cost):
        grid[x][y + 1] = cost + 1
        floodFill(grid, (x, y + 1))


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    floodFill(grid, (i, j))