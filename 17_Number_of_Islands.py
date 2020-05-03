class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        adjacents = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        visited = set()
        s = []
        count = 0
        
        l = len(grid)
        b = len(grid[0])
                
        for i in range(l):
            for j in range(b):
                
                if grid[i][j] == '1' and ((i, j) not in visited):
                    s.append((i, j))
                    visited.add((i, j))
                                        
                    while s:
                        node = s.pop()
                        
                        for adj in adjacents:
                            new_x = node[0] + adj[0]
                            new_y = node[1] + adj[1]
                            
                            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                                neigh = grid[new_x][new_y]
                                if neigh == '1' and (new_x, new_y) not in visited:
                                    visited.add((new_x, new_y))
                                    s.append((new_x, new_y))
                    count += 1
                    
        return count
