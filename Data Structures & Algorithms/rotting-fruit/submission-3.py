class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            minutes += 1
        
        return minutes if not fresh else -1