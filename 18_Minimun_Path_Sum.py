class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid or not len(grid):
            return 0
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j-1]

        return grid[-1][-1]
