class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        empty = True

        for r in grid:
            if 1 in r:
                empty = False

        if empty:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2

            minutes += 1
        
        for r in grid:
            if 1 in r:
                return -1
        
        return minutes - 1