class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0
        
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):

            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while q: 
                # popleft()
                row, col = q.popleft()
                
                # process: we want to check if each of the neighbor cells are valid
                # if the new cell is valid then we update queue
                for dr, dc in directions:
                    # update to neighbor pointer
                    nr, nc = row+dr, col+dc

                    # check if valid
                    if (
                        0<=nr<ROWS and 
                        0<=nc<COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"
                    ):
                        # update q
                        q.append((nr,nc))
                        visited.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
