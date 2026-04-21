class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        answer = 0

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))    
            visited.add((r, c))
            while q:
                qrow, qcol = q.popleft()
                for dr, dc in directions:
                    nr, nc = qrow+dr, qcol+dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))
                    



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited: 
                    bfs(r, c)
                    answer += 1
        return answer


        