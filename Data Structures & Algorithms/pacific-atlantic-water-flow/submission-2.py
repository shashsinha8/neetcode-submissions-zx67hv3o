class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        

        def bfs(sea_set):

            q = deque(sea_set)
            seen = set(sea_set)

            while q: 
                r, c = q.popleft()
                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nr, nc = r+dr, c+dc
                    
                    if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in seen and
                    heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            
            return seen

        pac_set = set()
        atl_set = set()
        for r in range(ROWS):
            pac_set.add((r, 0))
            atl_set.add((r, COLS-1))
        
        for c in range(COLS):
            pac_set.add((0, c))
            atl_set.add((ROWS - 1, c))

        # print(pac_flow, atl_flow)
        pac_flow = bfs(pac_set)
        atl_flow = bfs(atl_set)
        ans = [[r, c] for (r,c) in pac_flow & atl_flow]
        return (ans)
