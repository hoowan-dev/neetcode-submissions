WATER = "0"
UNVISITED = "1"
VISITED = "2"

def floodFill(grid: List[List[str]], coord: (int, int)) -> None:
    x, y = coord[0], coord[1]
    grid[x][y] = VISITED

    # up
    if (x - 1 >= 0) and (grid[x - 1][y] == UNVISITED):
        floodFill(grid, (x - 1, y))

    # down
    if (x + 1 < len(grid)) and (grid[x + 1][y] == UNVISITED):
        floodFill(grid, (x + 1, y))

    # left
    if (y - 1 >= 0) and (grid[x][y - 1] == UNVISITED):
        floodFill(grid, (x, y - 1))

    # right
    if (y + 1 < len(grid[x])) and (grid[x][y + 1] == UNVISITED):
        floodFill(grid, (x, y + 1))
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == UNVISITED:
                    floodFill(grid, (i, j))
                    numIslands += 1

        return numIslands