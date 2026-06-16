class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(reach, visited):
            q = deque(visited)
            while q: 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < ROWS and 
                        0 <= nc <COLS and 
                        heights[nr][nc] >= heights[r][c] and 
                        (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        reach[nr][nc] = 1
            

        reach_pac = [[0 if c != 0 and r!=0 else 1 for c in range(COLS)] for r in range(ROWS)]
        reach_atl = [[0 if c != COLS - 1 and r!= ROWS - 1 else 1 for c in range(COLS)] for r in range(ROWS)]
        
        visited_pac = set((r,c) for r in range(ROWS) for c in range(COLS) if reach_pac[r][c] == 1)
        visited_atl = set((r,c) for r in range(ROWS) for c in range(COLS) if reach_atl[r][c] == 1)

        bfs(reach_pac, visited_pac)
        bfs(reach_atl, visited_atl)


        for r in reach_pac:
            print(r)
        print(f"{visited_pac}\n")
        for r in reach_atl:
            print(r)
        print(f"{visited_atl}\n")

        return [[r, c] for r in range(ROWS) for c in range(COLS) if reach_pac[r][c] == 1 and reach_atl[r][c] == 1]

        
