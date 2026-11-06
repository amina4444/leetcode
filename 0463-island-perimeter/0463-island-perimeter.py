class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    perimeter += 4

                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        perimeter -= 2

                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        perimeter -= 2

        return perimeter
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        