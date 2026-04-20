class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0


        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    q = collections.deque()
                    q.append((r,c))
                    visited.add((r,c))
                    
                    # [r + 1, c]
                    # [r - 1, c]
                    # [r, c + 1]
                    # [r, c + 1]
                    while q:
                        row, col = q.popleft()
                        directions = [[1,0],[-1,0],[0,1],[0,-1]]
                        for dr, dc in directions: 
                            nr, nc = row+dr, col+dc 
                            if 0<=nr< rows and 0<=nc< cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                                q.append((nr, nc))
                                visited.add((nr, nc))
        return islands