class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]== "1" and (i, j) not in visited:
                    bfs(i, j)
                    res += 1
        
        return res
