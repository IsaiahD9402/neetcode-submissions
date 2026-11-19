class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid) 
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = collections.deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == "1":
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] == "1":
                                q.append((nr, nc))
                                visited.add((nr, nc))
                    res += 1
        
        return res
